(defun nth_elem(L N)
    (cond
        ((< N 0) nil)
        ((eq N 1)
            (car L)
        )
        (t
            (nth_elem (cdr L) (- N 1))
        )
    )
)

(write (nth_elem '(1 2 3 4 5 6) 6))
