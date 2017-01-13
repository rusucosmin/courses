(defun F(l)
    (max (car L) (caddr L))
)

(SETQ F 10)
(SETF G 'F)
(write (G '(8 11 2 3 7 9)))

(format t "~%")
(write f)
(format t "~%")
(write (function f))
(format t "~%")
(write  G)
