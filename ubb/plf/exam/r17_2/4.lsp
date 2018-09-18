(defun change(x lvl k)
    (cond
        ((atom x) (if (= lvl k) 0 x))
        (t (mapcar (lambda(el) (change el (+ 1 lvl) k)) x))
    )
)

(write (change '(a (1 (2 b)) (c (d))) 0 2))
(format t "~%")
(write (change '(a (1 (2 b)) (c (d))) 0 1))
(format t "~%")
(write (change '(a (1 (2 b)) (c (d))) 0 4))
(format t "~%")


