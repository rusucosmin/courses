(defun triple(x)
    (cond
        ((numberp x)
            (* x 3))
        ((atom x)
            x)
        (t
            (mapcar 'triple x))
    )
)

(write (triple '(1 2 3 4 5 6 ana (maria) (ce 1 2 3) (1 (3 4 rusu)))))
