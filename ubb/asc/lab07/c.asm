assume cs:code, ds:data

data segment
	a db 'bcdefgha'
	la equ $ - a
data end

code segment
start:
	mov ax, data
	mov ds, ax

	; swap(a[si], b[si])
	; a[si] = a[si] + b[si];
	; b[si] = a[si] - b[si]
	; a[si] = a[si] - b[si]

	
	;swap(ax, bx)
	;ax = ax + bx;
	;bx = ax - bx
	;ax = ax - bx

	

	LODS ;al
	

	mov ax, 4c00h
	int 21h
code end
end start
