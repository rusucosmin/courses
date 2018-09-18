assume cs:code, ds:data

data segment
	inputMsg db 'Please input the filename (including extension): $'
	maxFileName db 100
	lFileName db ?
	fileName db 100 dup(?), '$'
	writeErrorMsg db 'There was an error reading the file name!$'
	openErrorMsg db 'There was an error opening the file!$'
	msg db 'A message.'
	lgMsg db $ - msg
data ends

code segment
start:
	mov ax, data
	mov ds, ax

	;print the msg
	mov ah, 09h
	mov dx, offset inputMsg
	int 21h

	;read the filename from the user
	mov ah, 0ah
	mov dx, offset maxFileName
	int 21h

	mov bl, lFileName
	mov bh, 0
	mov fileName[bx], '0'

	;open the file
	mov ah, 3dh
	mov al, 2
	mov dx, offset fileName
	int 21h

	;handle the open exception
	jc openError

	mov bx, ax ;bx - file handle

	;move the pointer of the file
	mov ah, 42h
	mov al, 2
	mov cx, 0
	mov dx, 1
	int 21h

	;pointer to the end, write something
	mov ah, 40h	
	mov cl, lgMsg
	mov ch, 0
	mov dx, offset msg
	int 21h

	jc writeError
	; no error, finish
	jmp terminate

	openError:
		mov ah, 09h
		mov dx, offset openErrorMsg
		int 21h
		jmp terminate
	
	writeError:
		mov ah, 09h
		mov dx, offset openErrorMsg
		int 21h

	terminate:
	mov ax, 4c00h
	int 21h
code ends
end start
