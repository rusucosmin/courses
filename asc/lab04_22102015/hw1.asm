;Rusu Cosmin, gr 917 (attended lab 4 with gr 914), 22.10.2015, homework for lab 4, problem 2 unsigned representation
assume cs:code, ds:data

data segment

;Solution on unsigned representation
;Problem:
;2. 2/(a+b*c-9)+d
;a,b,c-byte; d-doubleword

; (a + b * c - 9) = word
	a db 10
	b db 2
	c db 3
	d dd 12
	x dd ?
data ends

code segment
start:
	mov ax, data
	mov ds, ax

	mov al, b 			; al = b
	mul c				; ax = b * c 

	mov bx, ax  		; bx = ax = b * c

	mov al, a 			; al = a
	cbw  				; ax = a

	add ax, bx			; ax = a + b * c

	mov bx, ax 			; bx = a + b * c
	
	mov al, 9 			; al = 9
	cbw 				; ax = 9
	sub bx, ax  		; bx = a + b * c - 9

	mov al, 2  			; al = 2
	cbw 				; ax = 2
	cwd 				; dx:ax = 2

	div bx  			; ax = dx:ax / bx
						; ax = 2 / (a + b * c - 9)
	cwd 				; dx:ax = 2 / (a + b * c - 9)

	mov bx, word ptr d
	mov cx, word ptr d + 2 ; cx:bx = d

	add ax, bx   
	adc dx, cx
	; dx:ax = dx:ax + cx:bx

	mov word ptr x, ax
	mov word ptr x + 2, dx
	
	mov ax, 4c00h
	int 21h
code ends
end start
