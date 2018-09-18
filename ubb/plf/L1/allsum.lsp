(defun sum(x)
    (cond
        ((null x) 0)
        ((numberp x) x)
        ((atom x) 0)
        (t
            (apply '+ (mapcar 'sum x))
        )
    )
)

(write (sum '(1 1 (1 ana (1 ana (1))))))
