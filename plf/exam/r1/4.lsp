(defun solve(x l k e)
    (cond
        ((atom x) (if (= k l) e x))
        (t (mapcar (lambda (el) (solve el (+ l 1) k e)) x))
    )
)

(write (solve '(a (b (g)) (c (d (e)) (f))) -1 3 'h))
