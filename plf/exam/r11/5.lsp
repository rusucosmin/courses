(defun liniarize(x)
    (cond
        ((numberp x) (list x))
        ((atom x) nil)
        (t (apply 'append (mapcar 'liniarize x)))
    )
)

(defun check(l)
    (cond
        ((null l) 0)
        (t (mod (car l) 2))
    )
)

(defun mcount(l)
    (cond
        ((atom l) 0)
        (t (+ (check (liniarize l)) (apply '+ (mapcar 'mcount l))))
    )
)

(write (mcount '(A (B 2) (1 C 4) (D 1 (5 F)) ((G 4) 6))))
