(defun cnt(L n k)
    (cond
        ((null L) 0)
        ((atom (car L)) (+ (if (= n k) 1 0) (cnt (cdr L) n k)))
        (t (+ (cnt (car L) (+ n 1) k) (cnt (cdr L) n k)))
    )
)

(write (cnt '(1 (2) (3 (4) (5))) 1 1))
(format t "~%") ;new line
(write (cnt '(1 (2) (3 (4) (5))) 1 2))
(format t "~%") ;new line
(write (cnt '(1 (2) (3 (4) (5))) 1 3))
(format t "~%")
;   arborele e asa:
;       1       level 1
;      /\
;     2  3      level 2
;        /\
;       4  5    level 3
