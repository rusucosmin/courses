(defun mremove(x lvl k)
    (cond
        ((atom x) (if (= k lvl) 0 x))
        (t (mapcar #'(lambda (el) (mremove el (+ 1 lvl) k)) x))
    )
)

(write (mremove '(a (1 (2 b)) (c (d))) 0 2))
(format t "~%")
(write (mremove '(a (1 (2 b)) (c (d))) 0 1))
