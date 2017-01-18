(defun mreplace(l e)
    (cond
        ((numberp l) e)
        ((atom l) l)
        (t (mapcar (lambda (el) (mreplace el e)) l))
    )
)

(defun mreplace2(l e)
    (cond
        ((null l) nil)
        ((numberp (car l)) (cons e (mreplace (cdr l) e)))
        ((atom (car l)) (cons (car l) (mreplace (cdr l) e)))
        (t (cons (mreplace (car l) e) (mreplace (cdr l) e)))
    )
)

(write (mreplace '(1 d (2 f (3))) 'ana))
(format t "~%")
(write (mreplace2 '(1 d (2 f (3))) 'ana))
