(defun toset(L)
    (cond
        (
            (null L)
                nil
        )
        (
            t
            (progn
                (setq act (toset (cdr L)))
                (cond
                    ((member (car L) act)
                        act)
                    (t
                        (cons (car L) act)
                    )
                )
            )
        )
    )
)

(write (toset '(1 2 3 1 2 3 6 7)))
