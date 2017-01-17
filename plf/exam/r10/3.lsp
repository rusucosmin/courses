(defun g(l)
    (+ (car l) (cadr l))
)

(setq h 'f)
(set h 'g)

(write (funcall f '(2 3 4 5 6)))
