assume cs:code, ds:data

data segment public

data ends

code segment public
public tipar
; Module to print on the screen the value stored in register AX
tipar:
	push ax
	push bx
	push cx
	push dx

	mov cx, 10
	mov bx, 0
	; Store the digits onto the stack
	; bx - number of digits
	; cx - base
	loopDigits:
		mov dx, 0
		div cx ; ax = ax / 10 dx = ax % 10
		push dx
		inc bx
		cmp ax, 0
		jne loopDigits
	
	;Print the digits from the stack
	mov cx, bx
	printDigits:
		pop dx
		add dl, '0'
		mov ah, 02h
		int 21h
	loop printDigits

	pop dx
	pop cx
	pop bx
	pop ax

	ret

code ends
end
