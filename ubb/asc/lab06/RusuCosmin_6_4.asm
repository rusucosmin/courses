;Rusu Cosmin, gr. 917, 16.10.2015, homework for lab 6, problem 4

;4. A byte string S of length l is given. Obtain the string D of length l-1 so that the elements of D represent the difference 
;   between every two consecutive elements of S.
;Exemple:
;S: 1, 2, 4, 6, 10, 20, 25
;D: 1, 2, 2, 4, 10, 5

assume cs:code, ds:data

data segment
	s db 1, 2, 4, 6, 10, 20, 25
	l equ $-s
	d db l - 1 dup(?)
data ends

code segment
start:
	mov ax, data
	mov ds, ax

	mov cx, l - 1
	mov si, 1
	mov di, 0
	mLoop:
		mov al, s[si]
		sub al, s[si - 1]
		mov d[si - 1], al
		inc si
		loop Mloop
	
	mov ax, 4c00h
	int 21h

code ends
end start
