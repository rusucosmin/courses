assume cs:code, ds:data

data segment public
	extrn sir : byte, ls : abs 
data ends

code segment public
extrn print: proc
start:
	mov ax, data
	mov ds, ax

	mov si, 0
	mov cx, word ptr ls

	jcxz sfarsit
	printNumbers:
		mov al, sir[si] 
		mov ah, 0
		call print	
		inc si
		loop printNumbers
	
	sfarsit:
	mov ax, 4c00h
	int 21h

code ends
end start
