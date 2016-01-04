assume cs:code, ds:data

data segment
	symbol db '0123456789ABCDEF'
	a dw 0bcdeh
	two dw 2
	ten dw 10
	sixteen dw 16

data ends

code segment

	printBase16 proc
		push ax
		push bx
		push cx
		push dx

		mov cx, 0

		loopDigits:
			mov dx, 0
			div sixteen
			push dx
			inc cx
			cmp ax, 0
			jne loopDigits

		mov bx,offset symbol
			
		printDigits:
			pop dx
			push ax

				mov al, dl
				xlat
				mov dl, al
				mov ah, 02h
				int 21h

			pop ax
		loop printDigits

		pop dx
		pop cx
		pop bx
		pop ax

		ret
	printBase16 endp

	printNewLine proc
		push ax
		push bx
		push cx
		push dx

		mov ah, 02h
		mov dl, 0ah
		int 21h
		mov dl, 0dh
		int 21h

		pop dx
		pop cx
		pop bx
		pop ax

		ret
	printNewLine endp

start:
	mov ax, data
	mov ds, ax

	mov ax, 3600
	call printBase16
	call printNewLine
	mov ax, 4c00h
	int 21h

code ends

end start
