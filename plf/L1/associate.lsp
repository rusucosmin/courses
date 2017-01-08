(defun associate(L1 L2)
    (cond
        ((null L1) nil)
        (t
            (cons (cons (car L1) (list (car L2))) (associate (cdr L1) (cdr L2)))
        )
    )
)

(write (associate '(1 2 3 4 5 6) '(2 4 6 8 10 12)))
