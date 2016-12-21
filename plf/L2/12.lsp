;12. Determine the list of nodes accesed
; in preorder in a tree of type (2).

;   preorder(L) = {
;       () if L = ()
;       (X) if n == 1
;       (L1) U preorder(L2) U preorder(L3) ... U preorder(Ln)
;   }

(defun preorder(x)
    (cond
        ((null x) nil)
        ((atom x) (cons x nil))
        (T (apply 'append (mapcar 'preorder x)))
    )
)
