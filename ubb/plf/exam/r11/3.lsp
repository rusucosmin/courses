(defun f(l)
    (cond
        ((null l) 0)
        ((> (f (cdr l)) 2) (+ (car l) (f (cdr l))))
        (t (f (cdr l)))
    )
)

(defun aux(v1 v2)
    (cond
        ((> v2 2) (+ v1 v2))
        (t v2)
    )
)

(defun g(l)
    (cond
        ((null l) 0)
        (t (aux (car l) (g (cdr l))))
    )
)


(write (f '(1 2 3 4 5 6 7)))
(format t "~%")
(write (g '(1 2 3 4 5 6 7)))
(format t "~%")
(write (f '(2 3 4 5 6 7)))
(format t "~%")
(write (g '(2 3 4 5 6 7)))
(format t "~%")
(write (f '(3 4 5 6 7)))
(format t "~%")
(write (g '(3 4 5 6 7)))
(format t "~%")





