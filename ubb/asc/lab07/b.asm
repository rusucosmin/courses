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
	mov si, 0
	mov di, 0

	loop1:
		mov al, byte ptr s[si]
		mov a[di], al
		inc di
		add si, 3	
		loop loop1

	while_loop:
		mov dx, 1
		mov si, 0
		mov di, 1
		mov cx, la - 1
		for_loop:
			mov al, a[si]
			mov bl, a[di]
			cmp al, bl
			jle lower_label
				mov al, a[si]
				mov bl, a[di]
				mov a[si], bl
				mov a[di], al
				mov dx, 0

			lower_label:
			inc si
			inc di
			loop for_loop
		cmp dx, 0
		je while_loop

	mov ax, 4c00h
	int 21h
code ends
end start
