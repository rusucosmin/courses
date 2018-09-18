ASSUME cs: code, ds:data

data SEGMENT
	a db -2
	b db -2
	x db ?
data ENDS
code SEGMENT

start:
	mov ax,data
	mov ds,ax

	mov al,a ; ax = a
	add al,b ; ax = ax + b
	mov x,al ; x = ax

	mov ax,4C00h
	int 21h
code ENDS
END start
