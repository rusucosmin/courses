# How to use this compiler

## Build it
First, you need to build the compiler
````
chmod +x make_comp.sh
./make_comp.sh
```

Now a `comp` executable should be created.

In order to compile a .cpp file, run:
```
./comp main.cpp
```

## Dosbox
Download dosbox from their [website](https://www.dosbox.com/wiki/DOSBox_and_Mac_OS_X0). Choose the
correct version based on you `OS`.
Run:
```
MOUNT C ~/path/to/your/asm/file
in my case:
MOUNT -u C
MOUNT C ~/courses/lftc/lab6
C:
cd tasm
cd bin
tasm /l /zi ..\..\out.asm
tlink /v out.obj io.obj
out.exe
```

## Run the test source codes

```
MOUNT C ~/courses/lftc/lab6
C:
cd tasm
cd bin
tasm /l /zi ..\..\test\test.asm
tlink /v test.obj io.obj
test.exe
```
