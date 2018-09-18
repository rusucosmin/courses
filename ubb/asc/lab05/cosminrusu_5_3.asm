;Rusu Cosmin, gr 917, 28.10.2015, homework for lab 5, problem 3
assume cs:code, ds:data

;Task:
; 3. The words A and B are given. Obtain the word C in the following way:
;- the bits 0-2 of C are the same as the bits 12-14 of A
;- the bits 3-8 of C are the same as the bits 0-5 of B
;- the bits 9-15 of C are the same as the bits 3-9 of A

data segment
	a dw 1010111001101100b
	b dw 0111110100100110b
	c dw ?
data ends

code segment
start:
	mov ax, data
	mov ds, ax

	;we will put the solution in register dx
	mov ax, a 					; ax = a
	and ax, 0111000000000000b  	; isolate the bits 12-14 from a
	shr ax, 12 					; move the isolated bits from 12-14 to 0-2
	mov dx, ax 					; this solves the first task
	; we solved the first task

	mov ax, b 					; ax = b
	and ax, 0000000000111111b 	; isolate the bits 0-5 from b
	shl ax, 3 					; move the isolated bits to 3-8
	or dx, ax 					; copy them into register dx

	;we solved the second task

	mov ax, a 					; ax = a
	and ax, 0000001111111000b   ; isolate the bits 3-9 from a
	shl ax, 6  					; move the isolated bits to 9-15
	or dx, ax 					; copy them into register dx

	mov c, dx 					; copy the result into the variable c

	;done - should be 1001 1011 0011 0010  binary which is:
				;     9    B    3    2     hexa

	mov ax, 4c00h
	int 21h
code ends
end start
