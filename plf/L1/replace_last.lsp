;c) Write a function to replace each sublist of a
;list with its last element.
; A sublist is an element from the first level,
;which is a list.
;  Example: (a (b c) (d (e (f)))) ==> (a c (e (f))) ==>
;(a c (f)) ==> (a c f)
;   (a (b c) (d ((e) f))) ==> (a c ((e) f)) ==> (a c f)

(defun tail(L)
    (cond
        ((null (cdr L)) (car L))
        (t (tail (cdr L)))
    )
)

(defun convert(L)
    (cond
        ((null L) nil)
        ((listp (car L)) (cons (tail (car L)) (convert (cdr L))))
        (t (cons (car L) (convert (cdr L))))
    )
)

(write (convert '(a (b c) (d (e (f))))))
(format t "~%")
(write (convert '(a c (e (f)))))
(format t "~%")
(write (convert '(a c (f))))
(format t "~%")
(write (convert '(a (b c) (d ((e) f)))))
(format t "~%")
(write (convert '(a c ((e) f))))

