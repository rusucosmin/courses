assume cs:code, ds:data

data segment
	a dd 1234h
	b dd 0AABBCCDDh
	x dd ?
data ends

code segment
start:
	mov ax, data
	mov ds, ax

		; dx:ax
		; cx:bx
	mov ax, word ptr a      ; ax = word(a)
	mov dx, word ptr a + 2  ; ax = word(a + 2);

	add ax, word ptr b     ; ax = ax + word(b)
	adc dx, word ptr b + 2  ; ax = ax + word(b + 2);

	mov word ptr x, ax
	mov word ptr x + 2, dx	;x = dx:ax

	mov ax, 4c00h
	int 21h
code ends
end start
