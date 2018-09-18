assume cs:code, ds:data

data segment
	;a dd 0aa00bf12h     ;a= 1010 1010 0000 0000 1011 1111 0001 0010
	; 5df ;     			0000 0000 0000 0000 0000 0110 1101 1111
	a dd 0fffffh 
	bmask dw ?
	nbits dw 0
data ends

code segment
start:
	mov ax, data
	mov ds, ax

	mov ax, word ptr a
	mov dx, word ptr a + 2

	mov cx, 16
	mov si, 0 	; this is where we keep the number of 1 bits from the representation
	cnt_biti_ax:
		dec cx
		mov bx, ax

		mov bmask, 1
		shl bmask, cl
		
		and bx, bmask

		cmp bx, 0
		jne incr_bits_ax
		jmp not_incr_ax
		incr_bits_ax:
			inc si
		not_incr_ax:

		inc cx
		loop cnt_biti_ax

	mov cx, 16

	cnt_biti_dx:	; now count the 1 bits from the dx register
		dec cx
		mov bx, dx

		mov bmask, 1
		shl bmask, cl
	
		and bx, bmask

		cmp bx, 0
		jne incr_bits_dx
		jmp not_incr_dx
		incr_bits_dx:
			inc si
		not_incr_dx:

		inc cx
		loop cnt_biti_dx

	mov nbits, si

	cmp si, 16
	ja invert
	jmp divide
		
	invert:
		xor ax, 0000000101010000b	
		xor dx, 0000001000000000b
		jmp end_of_pr		

	divide:

		mov cx, 2
		divide_by_two:
			sar dx, 1
			rcr ax, 1
			loop divide_by_two
	end_of_pr:	

	mov word ptr a, ax
	mov word ptr a + 2, dx
	mov ax, 4c00h
	int 21h
code ends
end start


for(int i = 0 ; i < 16 ; ++ i) {
	if(ax & (1 << i)) {
		++ cnt
	}
}
