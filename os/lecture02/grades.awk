BEGIN {
    print "Grade Averages"
    print "=============="
}

{
    sum[$1] = sum[$1] + $3
    num[$1] = num[$1] + 1
}

END {
    for(student in sum) {
        print student, sum[student]/num[student]
    }
}
