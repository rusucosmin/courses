(defun factorial(n)
    (cond ((zerop n) 1)
        (t ( * n (factorial (- n 1))))
    )
)

(setq n 3)
(write (factorial n))
