; problema. Se da un șir de doublewords, sa se construiască un șir de bytes ce cuprinde doar low byte-ul din high word-ul fiecărui doubleword, dar numai cu byte-urile negative. Apoi sa se afișeze fiecare byte din șirul creat in baza 2. Ex. Dacă am un dword 11AA2233h, high word ul e 11AAh, asta are low byte AAh și e negativ, deci îl pun în șir și afișez 10101010. Fac asa pentru fiecare dword din șir și pui în destinație și afișezi doar dacă byte ul e negativ.
; Ex: sir dd 12345678h,12ababcdh,FFfeFE33h
; your string should look like: AB,FE
; You should print on the screen: 1010 1011 1111 1110 (no space needed between the number)

assume cs:code, ds:data

data segment
	symbols db '0123456789abcdef'
	sir dd 12345678h, 12ababcdh, 0fffefe33h
	ls dw ($ - sir) / 4
	s db 100 dup (?)
data ends

code segment

print proc
	;procedure to print a number in a specific base
	;input: ax - the number to be converted
	;  		bx - the base we want to convert the number in
	push ax
	push bx
	push cx
	push dx

	mov cx, 0
	loopDigits:
		inc cx
		mov dx, 0
		div bx
		push ax
		push bx
		mov bx, offset symbols
		mov ax, dx
		xlat
		mov dx, ax
		pop bx
		pop ax
		push dx
		cmp ax, 0
		jne loopDigits

	printDigits:
		mov ah, 02h	
		pop dx
		int 21h
		loop printDigits	

;	mov ah, 02h
;	mov dl, ' '
;	int 21h

	pop dx
	pop cx
	pop bx
	pop ax
	ret
print endp

start:
	mov ax, data
	mov ds, ax

	mov cx, ls
	mov si, 2
	mov di, 0
	
	cmp cx, 0
	je sfarsit
	goOn:
		mov dl, byte ptr sir[si] 
		cmp dl, 0
		jge pozitiv
		mov s[di], dl
		mov dh, 0
		mov ax, dx
		mov bx, 2
		call print
		inc di
		pozitiv:
		add si, 4
		loop goOn

	
	sfarsit:	
	mov ax, 4c00h
	int 21h
code ends
end start
