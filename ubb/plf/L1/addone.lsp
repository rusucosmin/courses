(defun addone(L)
    (cond
        ((null (cdr L)) (if (= 9 (car L)) (cons 1 '(0)) (cons 0 (car L))))
        (t
            (progn
                (setq ret (addone (cdr L)))
                (setq tr (car ret))
                (setq act (cdr ret))
                (setq digit (car L))
                (if (= 10 (+ digit tr)) (cons 1 (cons 0 act)) (cons 0 (cons (+ digit tr) act)))
            )
        )
    )
)

(defun succ(L)
    (setq ret (addone L))
    (setq tr (car ret))
    (setq act (cdr ret))
    (if (= tr 1) (cons 1 act) act)
)

(write (succ '(1 9 3 5 9 9)))
(format t "~%")
(write (succ '(9 9 9 9 9 9)))
(format t "~%")
(write (succ '(1 9 9 9 9 9 9)))

