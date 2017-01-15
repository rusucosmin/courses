(defun solve(x lvl k e)
    (cond
        ((atom x) (if (= lvl k) e x))
        (t (mapcar (lambda(el) (solve el (+ 1 lvl) k e)) x))
    )
)

(write (solve '(a (b (g)) (c (d (e))(f))) -1 100 'h))
(format t "~%")
(write (solve '(a (b (g)) (c (d (e))(f))) -1 2 'h))
(format t "~%")
(write (solve '(a (b (g)) (c (d (e))(f))) -1 3 'h))
