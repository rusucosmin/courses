assume cs:code, ds:data

data segment
	symbol db '0123456789ABCDEF'
	buffer db 10, ?, 10 dup(?), '$'
	ten dw 10
data ends

code segment

printBase proc
	; Procedure to print the value stored in register ax in base bx from the set {2..16}
	push ax
	push bx
	push cx
	push dx

	mov cx, 0
	loopDigits:
		mov dx, 0
		div bx
		push dx
		inc cx
		cmp ax, 0
		jne loopDigits
	
	mov bx, offset symbol
	printDigits:
		pop dx
		mov al, dl
		xlat
		mov dl, al
		mov ah, 02h
		int 21h
		loop printDigits
	
	pop dx
	pop cx
	pop bx
	pop ax

	ret
printBase endp

printNewLine proc
	push ax
	push dx
	
	mov ah, 02h
	mov dl, 0ah
	int 21h
	mov dl, 0dh
	int 21h

	pop dx
	pop ax
	ret
printNewLine endp

readNumber proc
	; Procedure to read an integer from the user
	; returns it's value into the ax register
	push bx
	push cx
	push dx

	mov ah, 0ah
	mov dx, offset buffer
	int 21h

	mov si, 0
	mov cl, buffer[1]
	mov ch, 0

	mov ax, 0
	bucla:
		; ax = ax * 10 + a[i]
		mul ten
		mov bl, buffer[si][2]
		sub bl, '0'
		mov bh, 0
		add ax, bx
		inc si
		loop bucla

	pop dx
	pop cx
	pop bx

	ret

readNumber endp

start:
	mov ax, data
	mov ds, ax

	;mov ax, 01bcdh
	;mov bx, 2
	;call printBase
	call readNumber
	push ax ;push to the stack the first number

	call printNewLine

	call readNumber
	push ax ;push to the stack the second number

	pop bx ;the second one is the base
	pop ax ;the first one is the number that needs to be converted
	call printNewLine
	call printBase ;print ax in base bx

	mov ax, 4c00h
	int 21h

code ends
end start
