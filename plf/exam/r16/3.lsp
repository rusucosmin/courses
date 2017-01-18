;boring
(defun f(l)
    (cond
        ((null l) nil)
        ((listp (car l)) (addIfOk (f (car l)) (f (cdr l))))
        (t (list (car l)))
    )
)

(defun addIfOk(fcar fcdr)
    (append fcar fcdr (car fcar))
)

(write (f '((2 3) 100 (4 5))))
