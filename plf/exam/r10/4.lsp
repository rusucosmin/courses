(defun add(l n k)
    (write l)
    (format t "~%")
    (cond
        ((null l) nil)
        ((= (mod k n) 0) (cons (car l) (cons (car l) (add (cdr l) n (+ 1 k)))))
        (t (cons (car l) (add (cdr l) n (+ 1 k))))
    )
)

(write (add '(1 2 3 4 5) 2 1))
