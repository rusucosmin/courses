assume cs:code, ds:data

data segment
	a dw 12345
	digits dw 0
	base dw 0
	baseError db 'Input only 1 or 2.', 0ah, 0dh, '$'
	msgInput db 'Please input 1(for base 10), 2(for base 2)', 0ah, 0dh, '$' 
	newLine db 0ah, 0dh, '$' ; -new line character
data ends

code segment
start:
	mov ax, data
	mov ds, ax	
	
	mov ah, 09h
	mov dx, offset msgInput
	int 21h

	doIt:
		mov ah, 01h ; read a character; in al will have the results
		int 21h
		; print newline
		mov ah, 09h
		mov dx, offset newLine
		int 21h

		;compare al with '1', '2'.

		cmp al, '1'
		je base_10
		cmp al, '2'
		je base_2
		; then base is not recognised, print error message
		mov ah, 09h
		mov dx, offset baseError
		int 21h
		jmp doIt

	base_2:
		mov base, 2	
		jmp label2

	base_10:
		mov base, 10
	
	label2:
	mov ax, a
	mov dx, 0
	convert_base:
		inc digits
		div word ptr base
		push dx
		mov dx, 0
		cmp  ax, 0
		je print_conversion
		jmp convert_base
	
	print_conversion:
	mov cx, digits
	for_digits:
		mov ah, 02h	
		pop bx
		add bl, '0'
		mov dl, bl
		int 21h
		loop for_digits
	mov ax, 4c00h
	int 21h	
code ends
end start
