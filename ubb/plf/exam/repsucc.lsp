(defun msucc(x)
   (if (= (mod x 2) 0) (+ x 1) x)
)

(defun mreplace(L)
    (cond
        ((null L) nil)
        ((numberp (car L)) (cons (msucc (car L)) (mreplace (cdr L))))
        ((atom (car L)) (cons (car L) (mreplace (cdr L))))
        (t (cons (mreplace (car L)) (mreplace (cdr L))))
    )
)

(defun mreplacev2(x)
    (cond
        ((null x) nil)
        ((atom x) (if (numberp x) (msucc x) x))
        (t (mapcar 'mreplacev2 x))
    )
)

(write (mreplace '(1 s 4 (2 f (7)))))
(format t "~%")
(write (mreplacev2 '(1 s 4 (2 f (7)))))
