(defun liniarize(x)
    (cond
        ((null x) nil)
        ((atom x) (list x))
        (t (apply 'append (mapcar 'liniarize x)))
    )
)

(defun mlast (x)
    (cond
        ((null x) nil)
        ((not (numberp (car x))) (mlast (cdr x)))
        (t (if (null (mlast (cdr x))) (car x) (mlast (cdr x))))
    )
)

(defun check(l)
    (setq x (mlast (liniarize l)))
    (cond
        ((null x) 0)
        ((= (mod x 2) 1) 1)
        (t 0)
    )
)

(defun mcount(l)
    (cond
        ((atom l) 0)
        (t (+ (check l) (apply '+ (mapcar 'mcount l))))
    )
)

;Trebuie scazut -1 pentru ca ia in calcul si lista mare :)
(write (mcount '((a (b 2) (1 c 3) (d 1 (9 f)) ((g 7) 6)))))
