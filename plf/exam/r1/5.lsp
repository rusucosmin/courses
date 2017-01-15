(defun transform(l)
    (cond
        ((null l) nil)
        ((numberp l) (list l))
        ((atom l) nil)
        (t (apply 'append (mapcar 'transform l)))
    )
)

(defun check(l)
    (setq lin (transform l))
    (cond
        ((null lin) 0)
        ((numberp (car lin)) (- 1 (mod (car lin) 2)))
        (t nil)
    )
)

(defun solve(l)
    (cond
        ((null l) 0)
        ((atom l) 0)
        (t (progn
        (write l)
        (format t "~%")
        (write (check l))
        (format t "~%")
        (+ (check l) (apply '+ (mapcar 'solve l)))
        )
        )
    )
)

(write (check '(() (A 1000 2 3 4 (5 6 (7))))))
(write (solve '(A 3 (B 2) (1 C 4) (D 2 (6 F)) ((G 4) 6))))

