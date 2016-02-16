;La problema de la S4 sa se selecteze octetul de rang3 din fiecare dublucuvant care este divizibil cu 11, sa se aleaga 
;maximul dintre ele si sa se afiseze in baza 10

assume cs:code, ds:data

data segment
	sir dd 11223344h, 0aabbccddh, 0b0b0b0bh, 16161616h, 79797979h	
	ls equ $ - sir
	maxi db 0
data ends

code segment
start:
	mov ax, data
	mov ds, ax

	mov cx, ls
	mov si, 1

	cmp cx, 0
	je sfarsit
	loopBytes:
		mov dx, 0
		mov ax, 0
		mov al, byte ptr sir[si]
		push ax
		mov di, 11
		div di
		pop ax
		cmp dx, 0
		jne not_good
		divisible:
			cmp maxi, al
			jae not_good
			mov maxi, al
		
		not_good:
			add si, 4	
			loop loopBytes

	;print maxi
	
	mov ax, word ptr maxi
	mov bx, 10
	mov cx, 0

	loopDigits:
		mov dx, 0
		div bx
		push dx
		inc cx
		cmp ax, 0
		jne loopDigits

	printDigits:
		pop dx
		add dl, '0'
		mov ah, 02h
		int 21h
		loop printDigits

	sfarsit:
	mov ax, 4c00h
	int 21h
code ends
end start
