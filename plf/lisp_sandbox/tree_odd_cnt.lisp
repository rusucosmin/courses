(defun cnt(level l)
    (cond
        ((and (atom l) (= (mod level 2) 0)) 1)
        ((atom l) 0)
        (t (apply '+ (mapcar #'(lambda(x) (cnt (+ 1 level) x)) l)))
    )
)

(write (cnt 0 '(A (B) (C (D E)))))
