BEGIN {
    sum = 0
}

{
    sum = sum + $3;
    sum = sum + $4;
}

END {
    print sum;
}
