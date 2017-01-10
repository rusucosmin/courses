(defun gcdSmen(A B)
    (cond
        (
            (= B 0)
            A
        )
        (
            t
            (gcdSmen B (mod A B))
        )
    )
)

(defun gcdList(L)
    (cond
        (
            (NULL (CDR L))
            (cond
                (
                    (listp (car L))
                    (gcdList (car L))
                )
                (
                    T
                    (car L)
                )
            )
        )
        (
            (LISTP (CAR L))
            (gcdSmen (gcdList (CAR L)) (gcdList (CDR L)))
        )
        (
            t
            (gcdSmen (CAR L) (gcdList (CDR L)))
        )
    )
)

(write (gcdSmen 4 2))
(format t "~%")
(write (gcdList '(180 (60 120))))
