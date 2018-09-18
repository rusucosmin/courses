(defun isliniar(L)
    (cond
        ((null L) t)
        ((listp (car L)) nil)
        (t (isliniar (cdr L)))
    )
)

(write (isliniar '(1 2 3 4)))
(format t "~%")
(write (isliniar '(1 (2 3 4))))
