(defun maxodd(x k)
    (cond
        ((numberp x) (if (= (mod k 2) 0) -99999 x))
        ((atom x) -99999)
        (t (apply 'max (mapcar (lambda(el) (maxodd el (+ k 1))) x)))
    )
)

(defun check(l)
    (- 1 (mod (maxodd l 0) 2))
)

(defun mcount(l)
    (write l)
    (format t "~%")
    (write (check l))
    (format t "~%")
    (cond
        ((atom l) 0)
        (t (+ (check l) (apply '+ (mapcar 'mcount l))))
    )
)

; exemplul este prost; raspunsul corect e 6
(write (mcount '(a (b 2) (1 c 4) (1 (6 f)) (((g) 4) 6))))
