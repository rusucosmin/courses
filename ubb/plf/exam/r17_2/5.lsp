(defun sumodd(x lvl)
    (cond
        ((numberp x) (if (= (mod lvl 2) 0) 0 x))
        ((atom x) 0)
        (t (apply '+ (mapcar (lambda(el) (sumodd el (+ 1 lvl))) x)))
    )
)

(defun check(l)
    (- 1 (mod (sumodd l 0) 2))
)

(defun mcount(x)
    (cond
        ((atom x) 0)
        (t (+ (check x) (apply '+ (mapcar 'mcount x))))
    )
)

(write (mcount '(a 1 (b 2) (1 c 4) (d 1 (6 f)) ((g 4) 6))))
