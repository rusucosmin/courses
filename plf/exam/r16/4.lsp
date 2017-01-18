(defun mremove(l e)
    (cond
        ((null l) nil)
        ((atom (car l)) (if (eq (car l) e) (mremove (cdr l) e) (cons (car l) (mremove (cdr l) e))))
        (t (cons (mremove (car l) e) (mremove (cdr l) e)))
    )
)

(write (mremove '(1 (2 a (3 a)) (a)) 'a))
