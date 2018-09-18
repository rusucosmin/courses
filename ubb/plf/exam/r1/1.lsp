(defun f(l)
    (max (car l) (caddr l))
)

(setq f 10)
(setq g 'f)
(write (funcall g '(1 2 3 4 5 6)))
