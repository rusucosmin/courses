(defun F(L)
    (cond
        ((atom L) -1)
        ((> (F (car L)) 0) (+ (car L) (F (car L)) (F (cdr L))))
        (t (F (cdr L)))
    )
)

(defun add(el x1 x2)
    (cond
        ((> x1 0) (+ el x1 x2))
        (t x2)
    )
)

(defun FN(L)
    (cond
        ((atom L) -1)
        (t (add (car L) (F (car L)) (F (cdr L))))
    )
)

(write (f '(ana  4 5 6 7 8 9)))
(format t "~%")
(write (fn '(ana 2 3 4 5 6 7 8 9)))
(format t "~%")
(format t "~%")
(format t "~%")


