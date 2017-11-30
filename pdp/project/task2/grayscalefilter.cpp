#include <stdio.h>
#include <opencv2/opencv.hpp>
#include <vector>
#include <thread>
#include <mpi.h>

using namespace cv;
using namespace std;
inline int convertToInt(char *s) {
  string _s(s);
  stringstream str(_s);
  int x;
  str >> x;
  if(!str || x <= 0) {
    return -1;
  }
  return x;
}

inline void displayImage(Mat &image) {
  namedWindow("Display Image", WINDOW_OPENGL);
  imshow("Display Image", image);
  waitKey(0);
}

inline void apply_bw_filter(Mat &img, int st, int fn, int me) {
  cerr << "> proc " << me << " applying black & white filter\n";
  for (int i = st; i < fn; ++ i) {
    for (int j = 0; j < img.cols; ++ j) {
      Vec3b px = img.at<Vec3b>(i, j);
      int gray = (px[0] + px[1] + px[2]) / 3;
      px[0] = gray;
      px[1] = gray;
      px[2] = gray;
      img.at<Vec3b>(i, j) = px;
    }
  }
  cerr << "> proc " << me << " applied black & white filter\n";
}

inline void collect(Mat &img, int nrProcs) {
  cerr << "> master collects data";
  int rows = img.rows;
  int cols = img.cols;
  MPI_Status _;
  for (int i = 1; i < nrProcs; ++ i) {
    int st = i * rows / nrProcs;
    int dr = (i + 1) * rows / nrProcs;
    MPI_Recv(img.rowRange(st, dr).data, (dr - st) * cols * 3, MPI_BYTE, i, 3, MPI_COMM_WORLD, &_);
  }
  cerr << "> master collected data";
}

inline void master(Mat &img, int nrProcs) {
  cerr << "> master sending work to slaves\n";
  int rows = img.rows;
  int cols = img.cols;
  for (int i = 1; i < nrProcs; ++ i) {
    int st = i * rows / nrProcs;
    int dr = min(rows, (i + 1) * rows / nrProcs);
    int nr_rows = dr - st;
    MPI_Bsend(&nr_rows, 1, MPI_INT, i, 0, MPI_COMM_WORLD);
    MPI_Bsend(&cols, 1, MPI_INT, i, 1, MPI_COMM_WORLD);
    MPI_Ssend(img.rowRange(st, dr).data, nr_rows * cols * 3, MPI_BYTE, i, 2, MPI_COMM_WORLD);
  }
  apply_bw_filter(img, 0, rows / nrProcs, 0);
  collect(img, nrProcs);
  cerr << "> master sent work to slaves\n";
}

inline void slave(int me) {
  cerr << "> slave " << me << " started\n";
  int n, m;
  MPI_Status _;
  MPI_Recv(&n, 1, MPI_INT, 0, 0, MPI_COMM_WORLD, &_);
  MPI_Recv(&m, 1, MPI_INT, 0, 1, MPI_COMM_WORLD, &_);
  Mat chunk(n, m, CV_8UC3);
  MPI_Recv(chunk.data, n * m * 3, MPI_BYTE, 0, 2, MPI_COMM_WORLD, &_);
  apply_bw_filter(chunk, 0, n, me);
  MPI_Ssend(chunk.data, n * m * 3, MPI_BYTE, 0, 3, MPI_COMM_WORLD);
  cerr << "> slave finished";
}

int main(int argc, char** argv ) {
  srand(time(NULL));
  MPI_Init(0, 0);

  // get the current process id & the avaialble number of nodes
  int me;
  int nrProcs;
  MPI_Comm_size(MPI_COMM_WORLD, &nrProcs);
  MPI_Comm_rank(MPI_COMM_WORLD, &me);

  // check the current time
  clock_t t;
  t = clock();

  if (argc != 2) {
    printf("Usage: DisplayImage.out <Image_Path>\n");
    return -1;
  }
  string filename = argv[1];
  Mat image;
  image = imread(argv[1], CV_LOAD_IMAGE_COLOR);
  if (!image.data) {
    printf("No image data\n");
    return -1;
  }

  if(me == 0) {
    master(image, nrProcs);
    imwrite("grayscale.jpg", image);

    // get the total time took to perform the operations
    t = clock() - t;
    cout << "Applying grayscale filter to an image of "
        << image.rows << "x" << image.cols << " with " << nrProcs
        << " nodes took me " << t << " cycles ("
        << static_cast<float> (t) / CLOCKS_PER_SEC << " seconds)\n";

    cout << "Saved on grayscale.jpg\n";
  } else {
    slave(me);
  }
  MPI_Finalize();
  return 0;
}
