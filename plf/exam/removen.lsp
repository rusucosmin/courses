(defun mremove(L N P)
    (cond
        ((null L) nil)
        ((= (mod P N) 0) (mremove (cdr L) N (+ P 1)))
        (t (cons (car L) (mremove (cdr L) N (+ P 1))))
    )
)

(defun solve(L N)
    (mremove L N 1)
)

(write (solve '(1 2 3 4 5) 2))
