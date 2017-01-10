(defun is_member(X L)
    (cond
        (
            (null L)
            nil
        )
        (
            (listp (car L))
            (or (is_member X (car L)) (is_member X (cdr L)))
        )
        (
            (eq (car L) X)
            t
        )
        (
            t
            (is_member X (cdr L))
        )
    )
)

(write (is_member 7 '((1 2 3 4) (2 (1 (1 (1 (7))))) 3 4 5 6)))
