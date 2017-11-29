# Task 2

## How to run this task

First, this project uses `cmake` and `make`. Please make sure you have them installed.
Second, we will use `c++ 11` so make sure you have the correct and udpated `gcc` compiler]
installed.

For the image processing, we are using the OpenCV library (for loading / storing / writing images).
Install the library using the following command (on `macOS`)

We are using `OpenMPI 3.0` library for distributing the work among multiple nodes.
```bash
brew install opencv
```
This will also install the dependencies.

Install OpenMPI 3.0. Intruction on how to install it [here](https://wiki.helsinki.fi/display/HUGG/Open+MPI+install+on+Mac+OS+X).

Now run the following commands to build the project:
```bash
cmake .
make
```
A `GrayscaleFilter.o` executable file should be created by now.
In order to apply the grayscale filter to your image, run:
```
./GrayscaleFilter.o path_to_your_image number_of_threads
```
For example, run `mpirun --host localhost,localhost ./GrayscaleFilter.o ~/image.jpg' to apply
a filter to image.jpg on home dir with two nodes one on the localhost machine.

## Algorithm
We will have a master node that dicatates work to the other worker nodes.
After the master has distributed the work to the nodes, it keeps one part to himself,
solves it and then assembles all of the results together.

We split the image on row chunks. And each worker will get a chunk of image rows.
For example if we have the following matrix:
```
------row-0-------
------row-1-------
------row-2-------
------row-3-------
------row-4-------
------row-5-------
```
For `n = 3` nodes we can split the matrix in the following way:
```
------chunk-1-----
------chunk-1-----
------chunk-2-----
------chunk-2-----
------chunk-3-----
------chunk-3-----
```

First, the master will keep the first chunk (`chunk-1`), will send the two other
chunks to the slaves, will compute it's part and in the end collect the result from the
slaves.

## Synchronization
If the master finishes before the other nodes, he must wait for all of the others to finish. This
is automatically done by the `MPI_Recv()` method.

## Performance measurements
In order to test the perfomance, we can also make the master generate an arbitrary sized image.

