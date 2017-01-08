(defun depth(L)
    (cond
        ((null L)
            0)
        ((atom L)
            0)
        ((listp L)
            (+ 1 (apply 'max (mapcar 'depth L))))
    )
)

(write (depth '(1 ((2)) 3)))
