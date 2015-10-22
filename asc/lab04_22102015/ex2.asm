assume cs:code, ds:data

data segment
	a dd 1234h
	b dd 0aabbccddh
	x dd ?
data ends

code segment
start:
	mov ax, data
	mov ds, ax 

	mov ax, word ptr b
	mov dx, word ptr b + 2

	sub ax, word ptr a
	sbb ax, word ptr a + 2

	mov word ptr x, ax
	mov word ptr x + 2, dx

	mov ax, 4c00h
	int 21h;
code ends
end start
