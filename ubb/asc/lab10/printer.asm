assume cs:code, ds:data

data segment public
	sir dw 20, 01234h, 0, 15, 65530, 0111010111b
	final_sir label word
data ends

code segment public
extrn	tipar:proc
start:
	mov ax, data
	mov ds, ax

	mov si, offset sir
	cld
	bucla:
		cmp si, offset final_sir
		je final
		lodsw
		call tipar
	jmp bucla
	final:
	mov ax, 4C00h
	int 21h
code ends
end start