(defun mappend(x L)
    (cond
        ((null L) (list x))
        ((= x (car L)) L)
        (t (cons x L))
    )
)

(defun mmerge(L1 L2)
    (cond
        ((null L1) L2)
        ((null L2) l1)
        (t
            (progn
                (setq x1 (car L1))
                (setq x2 (car L2))
                (if (<= x1 x2) (mappend x1 (mmerge (cdr L1) L2)) (mappend x2 (mmerge L1 (cdr L2))))
            )
        )
    )
)

(write (mmerge '(1 2 3.5 4 5) '(-1 1 1 1 3 3.5 3.5 5 7)))
