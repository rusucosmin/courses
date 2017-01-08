(defun reverseall(L)
    (cond
        ((null L) nil)
        ((listp (car L)) (append (reverseall (cdr L)) (reverseall (car L))))
        (t
            (append (reverseall (cdr L)) (list (car L)))
        )
    )
)

(write (reverseall '(((A B) C) (D E))))
