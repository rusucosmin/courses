;read from the standard input (keyboard) the name of a file. Print the contents of this file on the screen.

assume cs:code, ds:data
data segment
	msg db 'Name of the file: $'
	maxFileName db 12
	lFileName db ?
	fileName db 12 dup (?)
	buffer db 100 dup (?), '$'
	openErrorMsg db 'File does not exist.$'
	readErrorMsg db "Can't read the file.$"
;	new db 0ah, 0dh, '$' - new line
data ends
code segment
start:
	mov ax, data
	mov ds, ax

	; print the string "msg" on the screen using interrupt 21h, function 09h
	mov ah, 09h
	mov dx, offset msg
	int 21h

	; read from the keyboard the name of the file using interrupt 21, function 0ah
	mov ah, 0ah
	mov dx, offset maxFileName
	int 21h
	; after the IHR is executed, the name of the file will be stored at the address maxFileName + 2 = fileName 
	; the byte from the offset maxFileName + 1 = lFileName will store the length (in characters) of the filename 

	

	; we transform the filename into an ASCIIZ string (put zero at the end)
	mov al, lFileName
	xor ah, ah
	mov si, ax
	mov fileName[si], 0

	; open the file using function 3dh of the interrupt 21h
	mov ah, 3dh
	mov al, 0 	; open the file for reading 
	mov dx, offset fileName
	int 21h

	jc openError ; CF will be set by the CPU if an error occured
	mov bx, ax ; save the file handle (which is put in AX by the RTI of int 21h, function 3dh) in bx
 
	; while we haven't reached the end of the file, we keep reading 100 bytes and display them on the screen 
	goOn:
		mov ah, 3fh
		mov dx, offset buffer
		mov cx, 100 	; we read maximum 100 characters
		int 21h
		jc readError	; the CPU sets CF=1 if an error occured

		; upon succes, the function 3dh returns in AX the number of read bytes
		; we save this number in SI and prepare the string for printing (add a '$' at the end)  
		mov si, ax
		mov buffer[si], '$'

		; print on the screen the text read with function 09h of interrupt 21h
		mov ah, 09h
		int 21h
		cmp si, 100
		je goOn ; if we had successfully read 100 bytes it means that we haven't reached the end of the file

 
	jmp endPrg 	; jump over the error handling code

	openError:		; print the openErrorMsg string using function 09h of interrupt 21h
		mov ah, 09h
		mov dx, offset openErrorMsg
		int 21h
		jmp endPrg 

	readError:		; print the readErrorMsg string using function 09h of interrupt 21h
		mov ah, 09h
		mov dx, offset readErrorMsg
		int 21h 

	endPrg:
		mov ax,4c00h
		int 21h
code ends
end start
