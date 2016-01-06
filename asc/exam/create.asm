assume cs:code, ds:data

data segment
	maxFileName db 100
	lFileName db ?
	fileName db 100 dup (?), '$'
	maxFileExt db 100
	lFileExt db ?
	fileExt db 100 dup (?), '$'
	fileNameMsg db 'Please input the file name: $'
	extMsg db 'Please input the extenstion: $'
	finalFile db 200 dup(?)

data ends

code segment
start:
	mov ax, data
	mov ds, ax

	mov ah, 09h
	mov dx, offset fileNameMsg
	int 21h

	;read filename
	mov ah, 0ah
	mov dx, offset maxFileName
	int 21h

	mov cl, lFileName
	mov ch, 0
	mov si, 0
	mov di, 0
	; move the file name
	putFileName:
		mov ah, fileName[si]
		mov finalFile[di], ah
		inc di
		inc si
		loop putFileName

	; put a '.'
	mov finalFile[di], '.'
	inc di

	mov ah, 02h
	mov dl, 0ah
	int 21h
	mov dl, 0dh
	int 21h

	mov ah, 09h
	mov dx, offset extMsg
	int 21h

	;read extension
	mov ah, 0ah
	mov dx, offset maxFIleExt
	int 21h

	mov cl, lFIleExt
	mov ch, 0
	mov si, 0

	putFileExt:
		mov ah, fileExt[si]
		mov finalFile[di], ah
		inc di
		inc si
		loop putFileExt

	mov finalFile[di], 0
	
	mov ah, 3ch
	mov al, 0 ;normal mode
	mov dx, offset finalFile
	int 21h

	mov ax, 4c00h
	int 21h
code ends
end start
