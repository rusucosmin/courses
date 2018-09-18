(defun removenil(l)
    (cond
        ((null l) nil)
        (t (if (null (car l)) (removenil (cdr l)) (cons (car l) (removenil (cdr l)))))
    )
)

(defun mappend(l x)
    (cond
        ((null l) nil)
        (t (cons x (car l)))
    )
)

(defun doIt(l x)
    (mappend (removenil l) x)
)

(defun pathh(x e)
    (cond
        ((atom x) (if (eq x e) (list e) nil))
        (t (doIt (mapcar (lambda (el) (pathh el e)) x) (car x)))
    )
)

(defun path(x e cur)
    (cond
        ((atom x) (if (eq x e) cur nil))
        (t (apply 'append (mapcar (lambda (el) (path el e (append cur (list (car x))))) x)))
    )
)


(write (path '(a (b (g)) (c (d (e)) (f))) 'e nil))
(format t "~%")
(write (path '(a (b (g)) (c (d (e)) (f))) 'v nil))
(format t "~%")
(write (path '(a (b (g)) (c (d (e)) (f))) 'f nil))
(format t "~%")
(write (path '(a (b (g)) (c (d (e)) (f))) 'b nil))
(format t "~%")
(write (path '(a (b (g)) (c (d (e)) (f))) 'v nil))
(format t "~%")


(write (pathh '(a (b (g)) (c (d (e)) (f))) 'e ))
(format t "~%")
(write (pathh '(a (b (g)) (c (d (e)) (f))) 'v ))
(format t "~%")
(write (pathh '(a (b (g)) (c (d (e)) (f))) 'f ))
(format t "~%")
(write (pathh '(a (b (g)) (c (d (e)) (f))) 'b ))
(format t "~%")
(write (pathh '(a (b (g)) (c (d (e)) (f))) 'v ))
(format t "~%")
