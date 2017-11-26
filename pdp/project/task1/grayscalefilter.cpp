#include <stdio.h>
#include <opencv2/opencv.hpp>
#include <vector>
#include <thread>

using namespace cv;

inline int convertToInt(char *s) {
  std::string _s(s);
  std::stringstream str(_s);
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

int main(int argc, char** argv ) {
  clock_t t;
  t = clock();
  if (argc != 3) {
    printf("Usage: DisplayImage.out <Image_Path> <Number_of_threads>\n");
    return -1;
  }
  std::string filename = argv[1];
  int T = convertToInt(argv[2]);
  if(T == -1) {
    printf("Please give me a valid integer for the number of threads\n");
    return -1;
  }
  Mat image;
  image = imread(argv[1], CV_LOAD_IMAGE_COLOR);
  if (!image.data) {
    printf("No image data\n");
    return -1;
  }
  std::vector <std::thread> th;
  for(int t = 0; t < min(image.rows, T); ++ t) {
    th.push_back(std::thread([&T, &t, &image](){
      for(int i = t; i < image.rows; i += T) {
        for(int j = 0; j < image.cols; ++ j) {
          Vec3b px = image.at<Vec3b>(i, j);
          int gray = (px[0] + px[1] + px[2]) / 3;
          px[0] = gray;
          px[1] = gray;
          px[2] = gray;
          image.at<Vec3b>(i, j) = px;
        }
      }
    }));
  }
  for(int i = 0; i < th.size(); ++ i) {
    th[i].join();
  }
  imwrite("grayscale.jpg", image);
//  displayImage(image);
  t = clock() - t;
  std::cout << "Applying grayscale filter to an image of "
      << image.rows << "x" << image.cols << " with " << T
      << " threads took me " << t << " cycles ("
      << static_cast<float> (t) / CLOCKS_PER_SEC << " seconds)\n";
  std::cout << "Saved on grayscale.jpg\n";
  return 0;
}
