(defun mmax(x)
    (cond
        ((numberp x) x)
        ((atom x) -999999)
        (t (apply 'max (mapcar 'mmax x)))
    )
)

(defun check(l)
    (- 1 (mod (mmax l) 2))
)

(defun solve(l)
    (cond
        ((atom l) 0)
        (t (+ (check l) (apply '+ (mapcar 'solve l))))
    )
)

(write (solve '(A (B 1) (1 C 4) 7 (D 1 (6 F)) ((G 4) 6))))
