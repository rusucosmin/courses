(defun odd(L)
    (cond
        ((null L) nil)
        (t (even (cdr L)))
    )
)
(defun even(L)
    (cond
        ((null L) t)
        (t (odd (cdr L)))
    )
)

(write (odd '(1 2 3 4 5)))
