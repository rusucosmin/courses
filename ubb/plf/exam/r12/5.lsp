(defun liniarize(l)
    (cond
        ((atom l) (list l))
        (t (apply 'append (mapcar 'liniarize l)))
    )
)

(defun check(l)
    (cond
        ((null l) 0)
        ((numberp (car l)) 0)
        (t 1)
    )
)

(defun mcount(l)
    (cond
        ((atom l) 0)
        (t (+ (check (liniarize l)) (apply '+ (mapcar 'mcount l))))
    )
)

(write (mcount '(1 a (b 2) (1 c 4) (d 1 (6 f)) ((g 4) 6))))
