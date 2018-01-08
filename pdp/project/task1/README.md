# Task 1

## How to run this task

First, this project uses `cmake` and `make`. Please make sure you have them installed.
Second, we will use `c++ 11` so make sure you have the correct and udpated `gcc` compiler]
installed.

For the image processing, we are using the OpenCV library (for loading / storing / writing images).
Install the library using the following command (on `macOS`)
```bash
brew install opencv
```
This will also install the dependencies.

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
For example, run `./GrayscaleFilter.o ~/image.jpg 2` to apply a filter to image.jpg on home dir
with 2 threads.

## Algorithm

## Synchronization

## Performance measurements

