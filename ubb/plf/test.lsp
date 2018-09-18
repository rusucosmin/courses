; Lisp 1
; mrev(L) = [] if L = []
; mrev(L) = mrev(L2..LN) if L1 is number
; mrev(L) = mrev(L2..LN) + L1 is atom
; mrev(L) = mrev(L2..LN) + mrev(L1) is list


(defun mrev(L)
    (cond
        ((null L) nil)
        ((numberp (car L)) (mrev (cdr L)))
        ((atom (car L)) (append (mrev (cdr L)) (list (car L))))
        (t (append (mrev (cdr L)) (mrev (car L))))
    )
)

(write (mrev '(((A B) 2 C) (A B C) 3 (D 1 E))))
(format t "~%")
(write (mrev '(A B C D E)))
(format t "~%")
(write (mrev '(A (((B C)) (X Y Z)) 2 D E)))

