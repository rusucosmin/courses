assume cs:code, ds:data

data segment
	a0 dd '12', '2'
	a1 db 12,34,56,78
	a2 dw 12h,34h,56h,78h
	a3 dw 1234h, 5678h
	a4 dd 1234h,5678h
	a5 dd 12345678h
	a6 dw 0abcdh
	a7 db '12','34','56','78'
	a8 db '12,34,56,78'
	a9 dw '12','34','56','78'
	a10 dw a2
	a11 db '$'
data ends

code segment
start:
	mov ax, data
	mov ds, ax

	mov ax, 4c00h
	int 21h

code ends
end start
