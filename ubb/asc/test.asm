assume cs:code, ds:data

data segment
	s db 'ab'
	d dd 0aaaah
	a db $ - a
data ends

code segment
start:
	mov ax, data
	mov ds, ax

	mov ax, '12'
	mov s, ah

	mov ax, 4c00h
	int 21h
code ends
end start
