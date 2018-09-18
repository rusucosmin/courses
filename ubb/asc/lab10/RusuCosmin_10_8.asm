;Rusu Cosmin, gr 917, 4.01.2016, homework for lab10, problem 8

;8. Print of the screen, for each number between 32 and 126, the value of the number (in base 10) and the character whose ASCII code the number is.

assume cs:code, ds:data

data segment public
data ends


code segment public
start:
extrn tipar:proc
	mov ax, data
	mov ds, ax

	; loop through the numbers between 32 and 126
	mov ax, 32
	goOn:
		;print ax
		call tipar

		;print the ascii code of ax
		mov dx, ax
		push ax
			mov ah, 02h
			int 21h
		pop ax

		push ax

		;print new line
		mov ah, 02h
		mov dl, 0ah
		int 21h
		mov dl, 0dh
		int 21h
		;end of print new line

		pop ax

		inc ax
		cmp ax, 127
		jne goOn 

	mov ax, 4c00h
	int 21h
code ends
end start
