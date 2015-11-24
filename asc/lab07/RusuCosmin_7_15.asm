;Rusu Cosmin, gr. 917, 23.10.2015, homework for lab07, problem 15

;15. A string of words is given. Build two strings of bytes, s1 and s2, in the following way: for each word, 
;- if the number of bits 1 from the high byte of the word is larger than the number of bits 1 from its low byte, 
;then s1 will contain the high byte and s2 will contain the low byte of the word
;- if the number of bits 1 from the high byte of the word is equal to the number of bits 1 from its low byte, then 
;s1 will contain the number of bits 1 from the low byte and s2 will contain 0
;- otherwise, s1 will contain the low byte and s2 will contain the high byte of the word.

assume cs:code, ds:data

data segment
	s dw 0abcdh, 1123h, 77abh, 0ab77h, 7788h
	ls equ ($ - s) / 2
	s1 db ls dup(00h)
	s2 db ls dup(00h)
	nb1 db 0
	nb2 db 0
	bmask db 0
data ends

code segment
start:
	mov ax, data
	mov ds, ax

	mov cx, ls 				; store the length of s in cx for the loop

	cmp cx, 0
	je end_label

	mov bp, 0

	mov si, 0
	mov di, 0

	main_loop:
		mov al, byte ptr s + bp
		mov ah, byte ptr s + bp + 1

		mov dl, 0
		mov nb1, dl
		mov nb2, dl

		push cx

			mov cx, 8
			bits_al:
				dec cx
				mov bl, 1
				shl bl, cl
				and bl, al
				cmp bl, 0
				je bit_is_zero_al
				; then, bit is one
				inc nb1

				bit_is_zero_al:
				inc cx
				loop bits_al
			
			mov cx, 8

			bits_ah:
				dec cx
				mov bl, 1
				shl bl, cl
				and bl, ah
				cmp bl, 0
				je bit_is_zero_ah
				inc nb2

				bit_is_zero_ah:
				inc cx
				loop bits_ah
			; s1->ah 
			; s2->al
			; s1->the byte with the most 1 bits
			; s2->the byte with the least 1 bits
		mov dl, nb1
		cmp dl, nb2 ; if(bits(al) > 
		je _equal ;if(bits(al) == bits(ah))
		ja _above  ;if(bits(al) > bits(ah))
			;else bits(al) < bits(AH)
			jmp _end_if
		_above:
			xchg al, ah
			jmp _end_if
		_equal:
			mov ah, nb1
			mov al, 0
		_end_if:
			mov s1[si], ah
			mov s2[si], al
			inc si
		pop cx
		add bp, 2
		loop main_loop
	end_label:

	mov ax, 4c00h
	int 21h
code ends
end start
