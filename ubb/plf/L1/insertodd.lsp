(defun insert (L A N)
    (progn
        (cond
            ((null L) nil)
            ((= N 1) (cons (car L) (cons A (insert (cdr L) A 0))))
            (t (cons (car L) (insert (cdr L) A 1)))
        )
    )
)

(defun insertodd(L A)
    (insert L A 0)
)

(write (insertodd '(1 2 3 4 5 6) "ana"))

