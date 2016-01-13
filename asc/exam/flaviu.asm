assume cs:code, ds:data

data segment
	msg1 db 'Sirul dat este :$'
	msg2 db 'Sirul citi este :$'
	buffer db 100, ?, 100 dup(?), '$'
	newline db 0ah, 0dh, '$'
data ends

code segment
start:
	mov ax, data
	mov ds, ax

	;printeaza primul sir
	mov ah, 09h
	mov dx, offset msg1
	int 21h

	;citeste sirul
	mov ah, 0ah
	mov dx, offset buffer
	int 21h

	;printeaza newline
	mov ah, 09h
	mov dx, offset newline
	int 21h

	;printeaza msg2
	mov ah, 09h
	mov dx, offset msg2
	int 21h

	;pune dolar la finalul sirului citit
	mov bl, buffer[1]
	mov bh, 0
	mov buffer[bx][2], '$'
	;printeaza sir
	mov ah, 09h
	mov dx, offset buffer + 2
	int 21h

	mov ax, 4c00h
	int 21h
code ends
end start
