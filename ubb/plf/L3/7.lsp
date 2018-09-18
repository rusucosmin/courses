;7. Write a function that substitutes an element
;E with all elements of a list L1 at all levels
;of a given list L

;
;   sub(L E Y) = {
;       () if L = ()
;       sub(L1 E Y) U sub(L2..LN E Y) if L1 is list
;       Y U sub(L2..LN E Y) if L1 == E
;       L1 U sub(L2..LN) otherwise

(defun sub(x e l1)
    (cond
        ((null x) nil)
        ((atom x) (if (eq x e) l1 x))
        (T (mapcar #'(lambda(y) (sub y e l1)) x))
    )
)

