(defun F(L)
    (cond
        ((atom L) -1)
        ((> (F (car L)) 0)(+ (car L)(F (car L)) (F (cdr L))))
        (T (f (cdr l)))
    )
)

(defun addIfYouCan(X Y Z)
    (cond
        ((> Y 0) (+X Y Z))
        (t Z)
    )
)

(defun Fsmen(L)
    (cond
        ((atom L) -1)
        (t (addIfYouCan (car L) (Fsmen (car L)) (Fsmen (cdr L))))
    )
)

///pare okay hmm, pls testeaza si tu si anunta-ma

(write (F '(1 2 3 4 5 6)))
(format t "~%")
(write (Fsmen '(1 2 3 4 5 6)))

