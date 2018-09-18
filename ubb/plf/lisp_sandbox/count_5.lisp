(defun transform(l)
    (cond
        ((null l) nil)
        ((numberp (car l)) (cons (car l) (transform (cdr l))))
        ((atom (car l)) (transform(cdr l)))
        (t (append (car l) (transform (cdr l))))
    )
)


(defun valid(l)
    (cond
        ((null (transform l)) nil)
        ((equal (car (transform l)) 5) t)
        (t nil)
    )
)

(defun cnt(l)
    (cond
        ((atom l) 0)
        ((valid l) (+ 1 (apply '+ (mapcar 'cnt l))))
        (t (apply '+ (mapcar 'cnt l)))
    )
)

(write (valid '(ana maria (5 6))))
(write (cnt '((5) (5 6) (5 7) (5 (5) 8))))
