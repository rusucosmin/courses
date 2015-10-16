;Rusu Cosmin, gr. 917, 14.10.2015, homework for lab 3, problem 13
assume cs:code, ds:data
;;m - [0, 100]
;h - [100, 300]
;yy - [0, 256]
;d - [-3, 15]
;
;(h+128)-(y+m+d) = h + 128 - y - m - d
;
;
;    Solution for Signed representation
;
;
data segment
	m db 10
	h dw 150
	yy dw 212
	d db -3
	x dw ?
data ends

code segment
start:
	mov ax, data
	mov ds,ax
	;signed representation
	mov bx,h ; bx = h
	mov ax,128 ; a = 128
	add bx,ax ; bx = h + ax = h + 128

	mov ax, yy ; ax = yy
	sub bx,ax ; bx = bx - ax = bx - yy

	mov al,m ; al = m, converts m into word 
	cbw

	sub bx,ax ; bx = bx - ax = bx - m

	mov al,d ; al = d, converts d into work
	cbw

	sub bx,ax

	mov x,bx

	mov ax,4C00h
	int 21h
code ends
end start
