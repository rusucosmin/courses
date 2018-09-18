;4. Se dadea un string de bytes ( in data segment), in care erau secvente de numere pozitive delimitate de 0 si trebuia calculata si afisata secventa de lungime maxima. (problema se rezolva multi modul) In a.asm se definea segmental si b.asm calcula secventa maxima.
;Ex: sir db 1,2,3,0,4,65,105,78,0 ,10,11,23,0
;Trebuia sa se afiseze : 4,65,105,78 (fara 0-ul din coada) (3 puncte)

assume cs:code, ds:data

data segment public
	symbols db '0123456789abcdef'
	extrn sir:byte
	extrn ls:word
	rasp dw 0
	maxi dw 0
data ends

code segment public

print proc
	;input
	; ax - number to be printed on the screen
	; bx - the base we want the number to be printed
	push ax
	push bx
	push cx
	push dx

	mov cx, 0

	loopDigits:
		mov dx, 0
		div bx
		push bx
		push ax
		mov bx, offset symbols
		mov ah, 0
		mov al, dl
		xlat
		mov dx, ax
		pop ax
		pop bx
		
		push dx

		inc cx

		cmp ax, 0
		jne loopDigits
	
	printDigits:
		mov ah, 02h
		pop dx
		int 21h
		loop printDigits

	mov ah, 02h
	mov dl, ' '
	int 21h

	pop dx
	pop cx
	pop bx
	pop ax
	ret
print endp

start:
	mov ax, data
	mov ds, ax

;	inc = 0
;	rasp = 0
;	for(int i = 0 ; i < n ; ++ i) {
;		if(a[i] == 0) {
;			nr = 0
;			inc = i + 1
;		}
;		else
;			++ nr
;		if(ans < nr)
;			ans = nr
;			rasp = inc
;		ans = max(ans, nr);

	mov cx, ls
	mov ax, 0 ;nr
	mov bx, 0 ;inc
	mov si, 0
	
	loopNumber:
		mov dl, sir[si]
		cmp dl, 0
		jne not_zero
		zero:
			mov ax, 0
			mov bx, si
			inc bx
			jmp get_maxim
		not_zero:
			inc ax

		get_maxim:
		cmp maxi, ax
		jae not_maxim
		mov maxi, ax
		mov rasp, bx
		not_maxim:	
		inc si	
		loop loopNumber
	
	mov si, rasp
	cmp sir[si], 0
	je sfarsit
	printNumbers:
		mov bx, 10
		mov al, sir[si]
		mov ah, 0
		call print
		inc si
		cmp sir[si], 0
		jne printNumbers

	sfarsit:
	mov ax, 4c00h
	int 21h
code ends
end start
