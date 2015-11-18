assume cs:code, ds:data

data segment
	a dw 1234h,5678h,90h
	la equ ($ - a) / 2
	b dw 4h,0abcdh,10h,1122h
	lb equ ($ - b) / 2
	c db la + lb dup(?)
	lc equ ($ - c)
data ends

code segment
start:
	mov ax, data
	mov ds, ax
	mov es, ax

	mov cx, la
	mov si, offset a

	mov di, offset c

	CLD

	loop1:
		LODSW
		STOSB
		loop loop1

	mov si, offset b
	inc si
	mov cx, lb

	loop2:
		LODSW
		STOSB
		loop loop2

	; now sort c

	;bool sorted = false;
	;while(!sorted) {
	;	sorted = true;
	;	for(int i = 0 ; i + 1 < n ; ++ i) {
	;		if(a[i] > a[i + 1]) {
	;			swap(a[i], a[i + 1]);
;				sorted = false;
;			}
;		}
;	}

	while_loop:
		mov dx, 1
		mov si, 0
		mov di, 1
		mov cx, lc - 1
		for_loop:
			CMPSB
			jle lower_label

				mov al, c[si]
				mov bl, c[di]
				mov c[si], bl
				mov c[di], al
				mov dx, 0

			lower_label:
			inc si
			inc di
			loop for_loop
		cmp dx, 0
		je while_loop

	mov ax, 4c00h
	int 21h
code ends
end start
