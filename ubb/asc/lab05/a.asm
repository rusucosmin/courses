assume cs:code, ds:data

data segment
	a dw 1010111001101100b
	b dw 0111110100100110b
	c dw ?
data ends

code segment
start:
	mov ax, data
	mov ds, ax

	mov dx, a
	and dx, 1b 		;isolate the bit 0 from a
	mov ax, a 		;ax = a 
	mov ax, 10b 	;isolate the bit 1 from a
	shl ax, 1 		;put the isolate bit 1 from a to pos 2
	or dx, ax 		;on bit 2 we put the bit 1 from a
	;we solved the task 1
	mov ax, b 		;ax = b
	and ax, 10b 	;isolate the bit 1 from b
	or dx, ax 		;put on the bit 1 the bit 1 from b
	;we solved the task 2
	or dx, 010111b 	;we put on the bits 3-5 the bits 0 1 0 corespondly
	;we solved task 3
	mov ax, a  		;ax = a
	and ax, 0111100000000000b ;we isolate the bits 11-14
	shr ax, 5 		;we move the bits to the positions 6-9
	or dx, ax 		;put the bits from 11-14 in a to 6-9 in dx
	;we solved task 4
	mov ax, b
	and ax, 0000000111111000b ;we isolate the bits 3-8 from b
	shl ax, 7 		;we put the bits 3-8 from b to bits 10-15 in ax
	xor ax, 1111110000000000b ;we flip the bits 10-15 in ax
	or dx, ax 		;we put the bits 10-15 from ax to 3-8 in ax

	mov c, dx 		;c = dx

	mov ax, 4C00h
	int 21h
code ends
end start
