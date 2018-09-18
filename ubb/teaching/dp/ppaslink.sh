#!/bin/sh
DoExitAsm ()
{ echo "An error occurred while assembling $1"; exit 1; }
DoExitLink ()
{ echo "An error occurred while linking $1"; exit 1; }
OFS=$IFS
IFS="
"
/usr/bin/ld /usr/lib/crt1.10.5.o       -x -multiply_defined suppress -L. -o triangle `cat link.res`
if [ $? != 0 ]; then DoExitLink ; fi
IFS=$OFS
