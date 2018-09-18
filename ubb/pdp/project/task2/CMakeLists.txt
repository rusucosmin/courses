cmake_minimum_required(VERSION 3.3)
set(CMAKE_CXX_STANDARD 11) # C++11...
set(CMAKE_CXX_STANDARD_REQUIRED ON) #...is required...
set(CMAKE_CXX_EXTENSIONS OFF) #...without compiler extensions like gnu++11
project(GrayscaleFilter)
# Open CV
find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})
add_executable(GrayscaleFilter.o grayscalefilter.cpp)
target_link_libraries(GrayscaleFilter.o ${OpenCV_LIBS})
# Pthread
set(THREADS_PREFER_PTHREAD_FLAG ON)
find_package(Threads REQUIRED)
target_link_libraries(GrayscaleFilter.o Threads::Threads)
# openMPI
find_package(MPI REQUIRED) #make it REQUIRED, if you want
include_directories(SYSTEM ${MPI_INCLUDE_PATH})
target_link_libraries(GrayscaleFilter.o ${MPI_CXX_LIBRARIES})
