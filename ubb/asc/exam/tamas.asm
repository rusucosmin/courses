assume cs:code, ds:data

data segment
	inputMsg db 'Please input the filename: $'
	maxFileName db 100
	lFileName db ?
	fileName db 100 dup(?), '$'
	vocals db 'aeiouAEIOU'
	nrv db $ - vocals
	fileHandle dw ?
	openErrorMsg db 'There was an error opening the file.$'
	readErrorMsg db 'There was an error reading the file.$'
	writeErrorMsg db 'There was an error writing to the file.$'
	buffer db 100 dup(0), '$'
	ten dw 10
data ends

code segment
start:
	mov ax, data
	mov ds, ax

	;ask for filename
	mov ah, 09h
	mov dx, offset inputMsg
	int 21h

	;read filename
	mov ah, 0ah
	mov dx, offset maxFileName
	int 21h

	;convert to asciiz
	mov bl, lFileName
	mov bh, 0
	mov fileName[bx], 0

	;open file
	mov ah, 3dh
	mov al, 2
	mov dx, offset fileName
	int 21h

	jc openError
	mov fileHandle, ax


	;read file & compute the number of vocals
	mov bx, fileHandle
	mov si, 0 

	loopFile:
		;read the buffer
		mov ah, 3fh
		mov cx, 100
		mov dx, offset buffer
		int 21h
		jc readError

		mov cx, ax
		push cx	

		loopBuffer:
			mov di, 0
			loopVocals:
				mov bx, cx
				dec bx
				mov dh, buffer[bx]
				cmp vocals[di], dh
				jne next_
				; if it wasn't a jump, increment si
				inc si
				next_:
				inc di
				cmp di, 10
				jne loopVocals
			dec cx
			cmp cx, 0
			jne loopBuffer

		pop cx
		cmp cx, 100
		je loopFile

	;put the digits into the stack
	mov ax, si
	mov cx, 0
	loopDigits:
		mov dx, 0
		div ten
		push dx
		inc cx
		cmp ax, 0
		jne loopDigits

	printDigits:
		pop dx
		push cx
		mov ah, 40h
		mov bx, fileHandle
		mov cx, 1
		add dl, '0'
		mov buffer[0], dl
		mov dx, offset buffer
		int 21h
		jc writeError
		pop cx
		loop printDigits

	;close the file
	jmp closeFile
		
	openError:
		mov ah, 09h
		mov dx, offset openErrorMsg
		int 21h
		jmp terminate

	readError:
		mov ah, 09h
		mov dx, offset readErrorMsg
		int 21h
		jmp closeFile
	
	writeError:
		mov ah, 09h
		mov dx, offset writeErrorMsg
		int 21h
	
	closeFile:
		mov ah, 3fh
		mov bx, fileHandle
		int 21h

	terminate:
	mov ax, 4c00h
	int 21h
code ends
end start
