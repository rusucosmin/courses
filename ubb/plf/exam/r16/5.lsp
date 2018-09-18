(defun sumodd(x k)
    (cond
        ((numberp x) (if (= (mod k 2) 0) 0 x))
        ((atom x) 0)
        (t (apply '+ (mapcar (lambda (el) (sumodd el (+ 1 k))) x)))
    )
)

(defun check(l)
    (- 1 (mod (sumodd l 0) 2))
)

(defun cnt(l)
    (cond
        ((atom l) 0)
        (t (+ (check l) (apply '+ (mapcar 'cnt l))))
    )
)

(write (cnt '(a 1 (b 2) (1 c 4) (d 1 (6 f)) ((g 4) 6))))
