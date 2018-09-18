;a) Write twice the n-th element of a linear list. 
;Example: for (10 20 30 40 50) and n=3 will produce 
;(10 20 30 30 40 50).

(defun twice(L n)
    (cond
        ((null L) nil)
        ((= n 1) (cons (car L) (cons (car L) (twice (cdr L) (- n 1)))))
        (t (cons (car L) (twice (cdr L) (- n 1))))
    )
)

(write (twice '(1 2 3 4 5 6 7) 10))

