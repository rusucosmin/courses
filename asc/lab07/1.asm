assume cs:code, ds:data

data segment
      s1 db 'bcx'
      l1 EQU $-s1
	  s2 db 'ade'
	  l2 EQU $-s2
	  s3 db l1 + l2 dup(?)
	  i dw 0
	  j dw 0
	  k dw 0
data ends

code segment
start:
	mov ax, data
	mov ds, ax

	mov es, ax
	mov cx, l1+l2

	/// ds:si
	/// es:di
	mov si, offset s1
	mov di, offset s2

	cld

	while_loop:
		cmpsb
		/// ja, je, jb	
		ja mai_mare
			
		jmp while_loop
		mai_mare:



	/**
		int i = 0;
		int j = 0;
		while(i <= n && j <= m) {
			if(A[i] <= B[j]) {
				++ k;
				C[k] = A[i];
				++ i;	
			}
			/// if(A[i] > B[j])
			else {
				++ k;
				C[k] = B[j];
				++ j;
			}
		while(i <= n) {
			++ k;
			C[k] = A[i];
			++ i;
		}
		while(j <= m) {
			++ k;	
			C[k] = B[j];
			++ j;
		}
		**/



	exit:

 	mov ah,4ch
	int 21
code ends
end start
