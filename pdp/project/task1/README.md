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

## Performance measurements
Run

```
chmod +x performance.sh
./performance.sh
```
Threads | Resolution(pixels) | Time
------- | ------------------ | ----
`1`|`100`|`.132956000`
`1`|`1000`|`.192965000`
`1`|`2000`|`.306282000`
`1`|`5000`|`1.372792000`
`1`|`10000`|`5.154087000`
`1`|`20000`|`20.120534000`
`3`|`100`|`.134055000`
`3`|`1000`|`.217861000`
`3`|`2000`|`.265310000`
`3`|`5000`|`1.024379000`
`3`|`10000`|`3.500031000`
`3`|`20000`|`12.669893000`
`5`|`100`|`.118544000`
`5`|`1000`|`.164585000`
`5`|`2000`|`.266334000`
`5`|`5000`|`1.002501000`
`5`|`10000`|`3.482809000`
`5`|`20000`|`12.838284000`
`10`|`100`|`.135131000`
`10`|`1000`|`.175655000`
`10`|`2000`|`.263338000`
`10`|`5000`|`.880799000`
`10`|`10000`|`3.296100000`
`10`|`20000`|`13.074761000`
`15`|`100`|`.123515000`
`15`|`1000`|`.143852000`
`15`|`2000`|`.238543000`
`15`|`5000`|`.894935000`
`15`|`10000`|`3.294234000`
`15`|`20000`|`12.572310000`
`25`|`100`|`.122487000`
`25`|`1000`|`.149807000`
`25`|`2000`|`.243321000`
`25`|`5000`|`.918178000`
`25`|`10000`|`3.091025000`
`25`|`20000`|`12.726595000`
`50`|`100`|`.115927000`
`50`|`1000`|`.147182000`
`50`|`2000`|`.230706000`
`50`|`5000`|`.918442000`
`50`|`10000`|`3.125228000`
`50`|`20000`|`12.114549000`
`100`|`100`|`.119749000`
`100`|`1000`|`.149140000`
`100`|`2000`|`.250897000`
`100`|`5000`|`.868255000`
`100`|`10000`|`3.202384000`
`100`|`20000`|`11.934701000`
`250`|`100`|`.129594000`
`250`|`1000`|`.166307000`
`250`|`2000`|`.250852000`
`250`|`5000`|`.894482000`
`250`|`10000`|`3.076837000`
`250`|`20000`|`12.005485000`
`500`|`100`|`.122462000`
`500`|`1000`|`.173370000`
`500`|`2000`|`.288964000`
`500`|`5000`|`.902318000`
`500`|`10000`|`3.090412000`
`500`|`20000`|`12.212828000`
