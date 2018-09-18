(defun createlist (x y)
    (cons x (cons y nil))
)

(defun appendtofr(E L)
    (cond
        ((null L) (cons (createlist E 1) nil))
        ((eq E (caar L)) (cons (createlist E (+ 1 (cadar L))) (cdr L) ))
        (t
            (cons (car L) (appendtofr E (cdr L)))
        )
    )
)

(defun freq(L)
    (cond
        ((null L) nil)
        (t
            (appendtofr (car L) (freq (cdr L)))
        )
    )
)

(write (freq '(A B A B A C A)))
