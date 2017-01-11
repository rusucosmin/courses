(defun mremove(L E)
    (cond
        ((null L) nil)
        ((atom (car L)) (if (eq (car L) E) (mremove (cdr L) E) (cons (car L) (mremove (cdr L) E))))
        (t (cons (mremove (car L) E) (mremove (cdr L) E)))
    )
)

;(if (cond) (then) (else))

(write (mremove '(1 2 (A B 3) (3)) 'A))
