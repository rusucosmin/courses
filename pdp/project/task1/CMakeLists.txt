cmake_minimum_required(VERSION 3.3)
set(CMAKE_CXX_STANDARD 11) # C++11...
set(CMAKE_CXX_STANDARD_REQUIRED ON) #...is required...
set(CMAKE_CXX_EXTENSIONS OFF) #...without compiler extensions like gnu++11
project(GrayscaleFilter)
# Open CV
find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})
add_executable(GrayscaleFilter grayscalefilter.cpp)
target_link_libraries(GrayscaleFilter ${OpenCV_LIBS})
# Pthread
set(THREADS_PREFER_PTHREAD_FLAG ON)
find_package(Threads REQUIRED)
target_link_libraries(GrayscaleFilter Threads::Threads)
