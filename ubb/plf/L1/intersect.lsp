(defun intersect(L1 L2)
    (cond
        ((null L1)
            nil)
        (t
            (progn
                (setq act (intersect (cdr L1) L2))
                (if (member (car L1) L2) (cons (car L1) act)act)
            )
        )
    )
)

(write (intersect '(1 2 3 4 5) '(1 2 3)))
