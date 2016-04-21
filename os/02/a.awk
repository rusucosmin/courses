BEGIN {
    sum = 0
}

/^r/ {
    print $0
    sum = sum + $3
}

END {
    print sum
}
