assume cs:code, ds:data

data segment
	inputMsgFile db 'Please input the filename: $'
	inputMsg db 'Please give a number or Q to end: $'
	yes db 'Is palindrom.$'
	no db 'Is not palindrom.$'
	maxFileName db 100
	lFileName db ?
	fileName db 100 dup(?)
	maxStrLen db 100
	strLen db ?
	mstr db 100 dup (?), '$'
	newLine db 0ah, 0dh, '$'
data ends

code segment

isPalindrom proc
	;procedure to check if the string str is palindrome or not (SETS the carry flag)
	mov si, 0
	push ax
	mov ax, 0
	mov al, strLen
	mov di, ax
	pop ax
	dec di
	loopDigits:
		push ax
		mov al, mstr[si]
		cmp al, mstr[di]
		pop ax
		jne notPalindrom
		inc si
		dec di
		cmp si, di
		jae loopDigits
	jmp palindrom
	notPalindrom:
		clc
		jmp sfarsit
	palindrom:
		stc
	sfarsit:
	ret
isPalindrom endp

start:
	mov ax, data
	mov ds, ax

	;print the input msg file
	mov ah, 09h
	mov dx, offset inputMsgFile
	int 21h

	;read the file name
	mov ah, 0ah
	mov dx, offset maxFileName
	int 21h

	;print newline
	mov ah, 09h
	mov dx, offset newLine
	int 21h
	
	;print the input msg
	mov ah, 09h
	mov dx, offset inputMsg
	int 21h

	;read the first number
	mov ah, 0ah
	mov dx, offset maxStrLen
	int 21h

	cmp mstr[0], 'Q'
	je inchide

	readNumbers:
		;check if it is palindrom
		call isPalindrom
		jnc notPal
		
		;print newline
		mov ah, 09h
		mov dx, offset newLIne
		int 21h

		mov al, strLen
		mov ah, 0
		mov si, ax
		mov mstr[si], '$'
		;print the number if is palindrom
		mov ah, 09h
		mov dx, offset mstr
		int 21h

		notPal:
		;read the number
		mov ah, 0ah
		mov dx, offset maxStrLen
		int 21h

		cmp mstr[0], 'Q'
		jne readNumbers


	inchide:
	mov ax, 4c00h
	int 21h
code ends
end start
