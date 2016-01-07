assume cs:code, ds:data

data segment
	a dw -32000
	b dw -32000
	abig dw 0
	maxFileName db 100
	lFileName db ?
	fileName db 100 dup(?), '$'
	inputFileHandle db 'Please input the filename: $'
	newLine db 0ah, 0dh, '$'
	fileHandle dw 0
	ten dw 10
	buffer db 100 dup (?), '$'
	
data ends

code segment

printToFile proc
	;function to print the value of the register dx:ax to the file whose fileHandle is in the register bx
	mov cx, 0
	loopDigits:
		div ten
		push dx
		mov dx, 0
		inc cx
		cmp ax, 0
		jne loopDigits
	
	printDigits:
		pop dx
		add dl, '0'
		mov buffer[0], dl
		mov ah, 40h
		push cx
		mov cx, 1
		mov dx, offset buffer
		int 21h
		pop cx
		loop printDigits
		
	ret
printToFile endp

start:
	mov ax, data
	mov ds, ax

	;print input msg
	mov ah, 09h
	mov dx, offset inputFileHandle
	int 21h

	;read fileName
	mov ah, 0ah
	mov dx, offset maxFileName
	int 21h

	;print newLine
	mov ah, 09h
	mov dx, offset newLine
	int 21h

	;put 0 at the end of the fileName : ASCIIZ
	mov bl, lFileName
	mov bh, 0
	mov fileName[bx], 0

	;create file
	mov ah, 3ch
	mov cx, 0
	mov dx, offset fileName
	int 21h

	mov fileHandle, ax

	;calculate the sum
	mov ax, a
	cwd
	mov abig, dx

	mov ax, b
	cwd

	add ax, a
	adc dx, abig

	cmp dx, 0
	jge pozitiv

	push ax
	push cx
	push dx

	;print -1 to the file
	mov bx, fileHandle
	mov buffer[0], '-'
	mov ah, 40h
	mov cx, 1
	mov dx, offset buffer
	int 21h

	pop dx
	pop cx
	pop ax

	negativ:
		xor dx, 0ffffh
		xor ax, 0ffffh

		add ax, 1
		adc dx, 0

	pozitiv:
		mov bx, fileHandle
		call printToFile

	mov ax, 4c00h

	int 21h
code ends
end start
