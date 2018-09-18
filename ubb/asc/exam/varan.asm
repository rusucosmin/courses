assume cs:code, ds:data

data segment
	maxFileName db 100
	lFileName db ?
	fileName db 100 dup (?), '$'
	inputMsgN db 'Please input n: $'
	inputMsgFile db 'Please input the name of the file: $'
	maxs db 10
	ls db ?
	s db 10 dup (?), '$'
	fileHandle dw ?
	newLine db 0ah, 0dh, '$'
	n db ?
	ten db 10
	readErrorMsg db 'Error while reading the file!$'
	writeErrorMsg db 'Error while writing to the file!$'
	openErrorMsg db 'Error while opening the file!$'
	buffer db 100 dup (?), '$'
	twentysix db 26
data ends

code segment

proc printString
	; prints on the screen a string which offset is stored in dx		
	mov ah, 09h
	int 21h
	ret
endp printString

proc readString
	; read a buffer from the user. It's starting addres is stoerd in dx
	mov ah, 0ah
	int 21h
	ret
endp

start:
	mov ax, data
	mov ds, ax

	;ask for n
	mov dx, offset inputMsgN
	call printString

	;read buffer for n
	mov dx, offset maxs
	call readString

	;put the value of n in ax
	mov cx, 0
	mov cl, ls
	
	mov ax, 0
	mov si, 0
	loopDigits:
		; n = n * 10 + buff[pos] - '0'
		mul ten
		mov bl, s[si]
		sub bl, '0'
		mov bh, 0
		add al, bl
		inc si
		loop loopDigits
	
	mov n, al

	;print newline
	mov dx, offset newLine
	call printString

	;ask for filename
	mov dx, offset inputMsgFile
	call printString

	;read buffer for the name of the file
	mov dx, offset maxFileName
	call readString

	;convert the filename to asciiz
	mov bx, 0
	mov bl, lFileName
	mov fileName[bx], 0

	;open the file
	mov ah, 3dh
	mov al, 2
	mov dx, offset fileName
	int 21h

	jc openError

	;store the fileHandle in fileHandle variable
	mov fileHandle, ax


	;read the file
	mov bx, fileHandle
	goOn:
		mov ah, 3fh
		mov cx, 100
		mov dx, offset buffer
		int 21h

		jc readError
		
		push ax ;store the length of the buffer in the stack
		mov si, ax
		mov cx, ax

		mov si, 0
		loopLetters:
			mov al, buffer[si]
			cmp al, 'a'
			jb next_
			cmp al, 'z'
			ja next_
			sub al, 'a'
			add al, n
			mov ah, 0
			div twentysix	; al = ax / 64
					; ah = ax % 64
			mov al, ah
			add al, 'a'
			mov buffer[si], al
			next_:
			inc si
			loop loopLetters

		pop ax ;pop the length of the buffer from the stack
		;push ax ;store it back in the stack
		;now move the pointer back ax times
		neg ax
		cwd
		mov cx, dx
		mov dx, ax
		mov ah, 42h
		mov al, 1
		int 21h


		;now write the files
		mov ah, 40h
		mov cx, si
		mov dx, offset buffer
		int 21h

		;now put back the pointer where it was before

;		pop ax
;		mov cx, 0
;		mov dx, ax
;		mov ah, 42h
;		mov al, 1
;		int 21h

		jc writeError

		cmp si, 100
		je goOn

	;errors
	jmp terminate
	openError:
		mov dx, offset openErrorMsg
		call printString
		jmp terminate

	readError:
		mov dx, offset readErrorMsg
		call printString
		jmp terminate

	writeError:
		mov dx, offset writeErrorMsg
		call printString

	terminate:
	mov ax, 4c00h
	int 21h
code ends
end start
