assume cs:code, ds:data

data segment public
	sir db 1, 12, 123, 89, 56
	ls equ $ - sir
data ends

code segment public
	
public print, sir, ls
print proc
	; input: ax - the number to be printed
	push ax
	push bx
	push cx
	push dx
	mov bx, 10
	mov cx, 0

	loopDigits:
		mov dx, 0
		div bx
		add dl, '0'
		push dx
		inc cx
		cmp ax, 0
		jne loopDigits
	
	printDigits:
		pop dx	
		mov ah, 02h
		int 21h
		loop printDigits
	
	mov dl, ' ';
	mov ah, 02h
	int 21h

	pop dx
	pop cx
	pop bx
	pop ax

	ret
print endp

code ends 
end
