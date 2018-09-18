#!/bin/bash

while read -p "Directory: " D; do
    if [ -d $D ]; then
        break
    fi
    echo "Not a directory" >&2
done

function f {
    local P=$1
    local F=$2
    local IAMLAST=$3

    S=""
    if [ -d $F ]; then
        S="/"
    fi

    echo "$P+- `basename $F`$S (`du -s -b $F | awk '{print $1}'`)"
    if [ -d $F ]; then
        L=""
        for C in $F/*; do
            L=$C
        done

        for C in $F/*; do
            if [ ! -e $C ]; then
                break
            fi
            VERT="|"
            if [ "$IAMLAST" = "last" ]; then
                VERT=" "
            fi

            LAST="not-really"
            if [ "$C" = "$L" ]; then
                LAST="last"
            fi
            f "$P$VERT   " $C $LAST
        done
    fi
}

f "" $D "last"
