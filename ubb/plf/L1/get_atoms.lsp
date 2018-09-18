(DEFUN get_atoms(L)
    (COND
        (
            (NULL L) NIL
        )
        (
            (LISTP (CAR L))
                (APPEND (get_atoms(CDR L)) (get_atoms(CAR L)))
        )
        (
            T
                (APPEND (get_atoms (CDR L)) (LIST (CAR L)))
        )
    )
)

(WRITE (get_atoms '((1 (2 (4 5))) 2  10 (11))))
(WRITE (get_atoms '(((A B) C) (D E))))

