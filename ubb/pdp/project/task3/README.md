# Task 3

## How to run this task

Import the `cl` and `cpp` files in a new `Xcode C++ Command-Line Utility` project.

For the image processing, we are using the OpenCV library (for loading / storing / writing images).
Install the library using the following command (on `macOS`)

We are using `OpenCL 1.1` with which XCode came with.
```bash
brew install opencv
```
This will also install the dependencies.

## Algorithm
The kernel takes a pixel and transforms it.

## Synchronization
Nothing, this is the coolest thing about `OpenCL`.

## Performance measurements
In order to test the perfomance, we can also generate or resize existing images.

