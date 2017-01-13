(defun F(l)
    (max (car L) (caddr L))
)

(SETQ F 10)
(SETQ G 'F)
(write (funcall G '(8 11 2 3 7 9)))
