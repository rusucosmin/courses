(defun dotproduct(L1 L2)
    (cond
        ((null L1)
            0)
        (t
        (+ (* (car L1) (car L2)) (dotproduct (cdr L1) (cdr L2))))
    )
)

(write (dotproduct '(1 2 3) '(1 2 3)))
