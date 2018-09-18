(defun madd(L N K)
    (cond
        ((null L) nil)
        ((= (mod K N) 0) (cons (car L) (cons (car L) (madd (cdr L) N (+ K 1)))))
        (t (cons (car L) (madd (cdr L) N (+ 1 K))))
    )
)

(write (madd '(1 2 3 4 5) 6 1))
