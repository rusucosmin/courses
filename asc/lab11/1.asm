;Read from the keyboard a string s of characters and a byte n. Divide the string s 
;in n sub-strings (the last sub-string can have less than n characters). Print on 
;the screen each sub-string and its position in the string. 

;Example: 
;Input: s = '1234567890abcdefg', n = 4
;Output:
;1: '1234'
;2: '5678'
;3: '90ab'
;4: 'cdef'
;5: 'g'

assume cs:code, ds:data

data segment public
	msg1 db 'Please insert the string s: $'
	s db 200, ?, 200 dup(?)
	msg2 db 'Plase insert the number n: $'
	n_str db 4, ?, 3 dup(?)
	n db ?
	newLine db 10
	ten db 10
data ends

code segment public
extrn tipar: proc
start:
	mov ax, data
	mov ds, ax

	;print msg1
	mov ah, 09h
	mov dx, offset msg1
	int 21h
	
	;read s
	mov ah, 0ah
	mov dx, offset s
	int 21h

	;print newline
	mov ah, 02h
	mov dl, newLine 
	int 21h

	;print msg2
	mov ah, 09h
	mov dx, offset msg2
	int 21h

	;read n
	mov ah, 0ah
	mov dx, offset n_str
	int 21h

	;print newline
	mov ah, 02h
	mov dl, newLine
	int 21h

	;now convert the number from string to an integer
	mov cl, n_str[1]
	mov ch, 0
	mov si, offset n_str + 2
	CLD

	mov ax, 0
	
	loopDigits:
		;store ax
		push ax
		lodsb
		;ax = ax * 10 + s[i] - '0'
		mov bl, al
		sub bl, '0'
		mov bh, 0
		;retrieve ax
		pop ax
		mul ten
		add ax, bx
	loop loopDigits
	
	mov n, al

	mov cl, s[1]	
	mov ch, 0
	mov si, 0

	mov di, 1
	mov ax, di
	call tipar

	loopString:
		cmp si, 0
		je not_zero
		mov ax, si		
		div n
		cmp ah, 0
		jne not_zero
		;if it is zero, print new line
		
		mov ah, 02h
		mov dl, newline
		int 21h

		;then, print the number of lines
		inc di
		mov ax, di
		call tipar

		not_zero:	
			mov ah, 02h
			mov dl, s[si][2]
			int 21h	

			inc si
			loop loopString

	mov ax, 4c00h
	int 21h
code ends
end start
