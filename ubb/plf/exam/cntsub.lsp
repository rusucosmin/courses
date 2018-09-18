(defun transform(x)
    (cond
        ((null x) nil)
        ((atom x) x)
        (t (apply 'append (mapcar 'transform x)))
    )
)

(defun check(x)
    (cond
        ((null x) 0)
        ((null (cdr x)) (if (numberp (car x)) 0 1))
        (t (check (cdr x)))
    )
)

(defun cntsub(x)
    (cond
        ((null x) 0)
        ((atom x) 0)
        (t (+ (check x) (apply '+ (mapcar 'cntsub x))))
    )
)

(write (cntsub '(A (B 2) (1 C 4) (D 1 (6 F)) ((G 4) 6) F)))
(write (cntsub '(A (B C) (D E) (F G))))
