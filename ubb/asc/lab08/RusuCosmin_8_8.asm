;Rusu Cosmin - gr. 917, 26.11.2015, homework for lab08, problem 08

;8. Write a program which reads the name of a file and two characters from the keyboard. 
;The program should replace all occurrences of the first character in that file with the 
;second character given by the user.

assume cs:code, ds:data

data segment
	msg db 'Name of the file: $'
	msgCh1 db 'Character to replace: $'
	msgCh2 db 'New character: $'
	ch1 db ?
	ch2 db ?
	maxFileName db 12
	lFileName db ?
	fileName db 12 dup (?)
	buffer db 100 dup (?), '$'
	openErrorMsg db 'File does not exist.$'
	readErrorMsg db "Can't read the file.$"
	newLine db 0ah, 0dh, '$' ; \n character
data ends

code segment
start:
	mov ax, data
	mov ds, ax

	; print the string 'msg' to the screen
	mov ah, 09h
	mov dx, offset msg
	int 21h

	;read from the keyboard the name of the file
	mov ah, 0ah
	mov dx, offset maxFileName
	int 21h

	;print newline
	mov ah, 09h
	mov dx, offset newLine
	int 21h

	;print msgCh1
	mov ah, 09h
	mov dx, offset msgCh1
	int 21h

	;read first character
	mov ah, 01h
	int 21h
	mov ch1, al

	;print newline
	mov ah, 09h
	mov dx, offset newLine
	int 21h

	;print msgCh2
	mov ah, 09h
	mov dx, offset msgCh2
	int 21h

	;read second character
	mov ah, 01h
	int 21h
	mov ch2, al

	;print newline
	mov ah, 09h
	mov dx, offset newLine
	int 21h

	mov al, lFileName
	xor ah, ah
	mov si, ax
	mov fileName[si], 0

	;open the file
	mov ah, 3dh
	mov al, 0
	mov dx, offset fileName
	int 21h

	jc openError 
	mov bx, ax

	goOn:
		mov ah, 3fh
		mov dx, offset buffer
		mov cx, 100
		int 21h
		jc readError

		mov si, ax
		mov buffer[si], '$'

		mov cx, ax
		mov di, 0
		; now iterate through the buffer and change the letters where needed
		replace_ch:
			mov ah, ch1
			mov al, ch2
			cmp buffer[di], ah 
			jne _nu
				mov buffer[di], al 
			_nu:
			inc di
			loop replace_ch

		mov ah, 09h
		int 21h
		cmp si, 100

		je goOn
	
	jmp endPrg

	openError:
		mov ah, 09h
		mov dx, offset openErrorMsg
		int 21h
		jmp endPrg
	
	readError:
		mov ah, 09h
		mov dx, offset readErrorMsg
		int 21h
	
	endPrg:
		mov ax, 4c00h
		int 21h
code ends
end start
