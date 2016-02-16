data segment
	a dw 10
	b dw 20
data ends

code segment
start:
	mov ax, data
	mov ds, ax

	mov ax, data:a

	mov ax, 4c00h
	int 21h
code ends
end start


