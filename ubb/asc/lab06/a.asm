ASSUME cs:code, ds:data

data segment
	n db 10
	x dw ?
data ends

code segment
start:
	mov ax, data
	mov ds, ax

	mov cx, word ptr n
	mov ax, 0

	jcxz end_of_program

	bucla:
		add ax, cx
		loop bucla

	end_of_program:
		mov x, ax	
	
	mov ax, 4c00h
	int 21h
code ends
end start
