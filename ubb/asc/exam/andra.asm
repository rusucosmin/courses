assume cs:code, ds:data

data segment
	newdir db 'director/altdir', 0
data ends

code segment
start:
	mov ax, data
	mov ds, ax

	mov ah, 3Ah
	mov dx, offset newdir
	int 21h

	mov ax, 4c00h
	int 21h
code ends
end start
