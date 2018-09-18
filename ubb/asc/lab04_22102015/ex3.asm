assume cs: code, ds:data

data segment
	a db 10h
	b db 10h
	d db 10h
	c dd 0h
	x dw ? 
data ends

;3. x = (a * b - c) / d, where a,b,d - byte and c - double-word



; [(nr + 6) % 30] + 1
; nr = 25

code segment
start:
	mov ax, data
	mov ds, ax

	mov al, a ; al = a
	imul b ; ax = a * b
	cwd ; extend ax to dx:ax

	sub ax, word ptr c 
	sbb dx, word ptr c + 2
	; dx:ax = a * b - c

	idiv word ptr d

	;ax = (a * b - c) / d
	mov x, ax

	mov ax, 4c00h
	int 21h
code ends
end start
