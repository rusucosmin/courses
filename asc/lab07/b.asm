assume cs:code, ds:data

data segment
	s dd 12345678h,5bcfh,45327h,1798dfeh,0f112233h
	ls equ $ - s
	a db (ls + 2) / 3 dup(?)
	la equ $ - a

data ends

code segment
start:
	mov ax, data
	mov ds, ax
	mov es, ax

	mov cx, la
	loop1:
		
		loop loop1



	mov ax, 4c00h
	int 21h
code ends
end start
