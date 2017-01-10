(defun dfs(node cnt level m_list)
    (write node)
    (write level)
        (cond
        ((null m_list)
            nil
        )
        ((= cnt 0)
            m_list)
        (T
            (setq son (dfs (car m_list) (car (cdr m_list)) (+ level 1) (cdr (cdr m_list))))
            (dfs node (- cnt 1) level son))
    )
)

(dfs 'A 2 1 '(B 0 C 2 D 0 E 0))
