(defun nlist(L)
    (cond
        ((null L) 1)
        ((listp (car L)) (+ (nlist (car L)) (nlist (cdr L))))
        (t (nlist (cdr L)))
    )
)

(write (nlist '(1 2 (3 (4 5) (6 7)) 8 (9 10))))
