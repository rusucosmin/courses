assume cs:code, ds:data

data segment
	maxFileName db 100
	lFileName db ?
	fileName db 100 dup(?), '$'
	buffer db 100 dup(?), '$'
	readMsg db 'There was an error reading the file.$'
	openMsg db 'There was an error opening the file.$'
data ends

code segment
start:
	mov ax, data
	mov ds, ax

	;read the fileName from user
	mov ah, 0Ah
	mov dx, offset maxFileName
	int 21h
	
	;print new line
	mov ah, 02h
	mov dl, 0ah
	int 21h
	mov dl, 0dh
	int 21h
	
	;convert string to asciiz
	;put 0 at the end of array
	;for print only
	mov bx, 0
	mov bl, lFileName
	mov fileName[bx], 0

	mov ah, 3dh
	mov al, 0 ; read
	mov dx, offset fileName
	int 21h
	; now ax contains the handle for the file
	jc openError
	
	mov bx, ax
	readBuffer:
		;read 100 characters
		mov ah, 3fh
		mov dx, offset buffer
		mov cx, 100
		int 21h
		
		jc readError
		
		mov si, ax
		mov buffer[si], '$'

		mov ah, 09h
		int 21h
		cmp si, 100
		je readBuffer

	jmp terminate

	openError:
		mov ah, 09h
		mov dx, offset openMsg
		int 21h
		jmp terminate

	readError:
		mov ah, 09h
		mov dx, offset readMsg
		int 21h

	terminate:
	mov ax, 4c00h
	int 21h
code ends
end start
