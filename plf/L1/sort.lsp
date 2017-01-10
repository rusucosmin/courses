(defun insert(E L)
    (cond
        ((null L)
            (list E))
        ((< E (car L))
            (cons E L))
        (t
            (cons (car L) (insert E (cdr L)))
        )
    )
)

(defun msort(L)
    (cond
        ((null L)
            nil)
        (t
            (insert (car L) (msort (cdr L)))
        )
    )
)

(write (msort '(3 2 1 9 8 1)))
