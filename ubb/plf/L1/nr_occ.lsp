(defun nr_occ(L X)
    (cond
        (
            (null L)
            0
        )
        (
            (listp (car L))
                (+ (nr_occ (car L) X) (nr_occ (cdr L) X))
        )
        (
            (eq (car L) X)
            (+ 1 (nr_occ (cdr L) X))
        )
        (
            t
            (nr_occ (cdr L) X)
        )
    )
)

(write (nr_occ '(1 2 3 4 5 2 2 1 1 2) 2))
(format t "~%")
(write (nr_occ '() 2))
