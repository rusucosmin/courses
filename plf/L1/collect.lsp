(defun collect_list(L)
    (cond
        (
            (null L)
            nil
        )
        (
            (atom (car L))
            (collect_list (cdr L))
        )
        (
            t
            (cons (car L) (append (collect_list (car L)) (collect_list (cdr L))))
        )
    )
)

(defun collect(L)
    (cons L (collect_list L))
)

(write (collect '(1 2 (3 (4 5) (6 7)) 8 (9 10))))
