assume cs:code, ds:data

data segment
	a dw 1
	b dw 10
data ends

code segment
start:
	mov ax, data
	mov ds, ax

	mov bx, a
	mov ax, [bx]
	mov ax, 4c00h
	int 21h
code ends
end start
