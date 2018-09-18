assume cs:code, ds:data

data segment
	n db 15
	sum dw ?
	aux dw ?
data ends

code segment
start:
	mov ax, data
	mov ds, ax

	; ax = sum
	; cs
	; bx = actualul
	; dx = precedentul

	mov cx, word ptr n

	dec cx
	dec cx

	mov bx, 1
	mov dx, 0
	mov ax, 1
	
	bucla:
		mov aux, bx
		add bx, dx
		mov dx, aux
		add ax, bx	
		loop bucla

	mov sum, ax

	mov ax, 4c00h
	int 21h
code ends
end start
