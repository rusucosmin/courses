	.file	"m1.c"
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"zero"
	.text
	.globl	zero
	.type	zero, @function
zero:
.LFB27:
	.cfi_startproc
	pushq	%rbx
	.cfi_def_cfa_offset 16
	.cfi_offset 3, -16
	movl	$0, %ebx
.L4:
	movl	$mtx, %edi
	call	pthread_mutex_lock
	cmpl	$0, turn(%rip)
	jne	.L2
	movl	$.LC0, %edi
	call	puts
	movl	$1, turn(%rip)
	addl	$1, %ebx
.L2:
	movl	$mtx, %edi
	call	pthread_mutex_unlock
	cmpl	$99, %ebx
	jle	.L4
	movl	$0, %eax
	popq	%rbx
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE27:
	.size	zero, .-zero
	.section	.rodata.str1.1
.LC1:
	.string	"o"
	.text
	.globl	one
	.type	one, @function
one:
.LFB28:
	.cfi_startproc
	pushq	%rbx
	.cfi_def_cfa_offset 16
	.cfi_offset 3, -16
	movl	$0, %ebx
.L9:
	movl	$mtx, %edi
	call	pthread_mutex_lock
	cmpl	$1, turn(%rip)
	jne	.L7
	movl	$.LC1, %edi
	call	puts
	movl	$0, turn(%rip)
	addl	$1, %ebx
.L7:
	movl	$mtx, %edi
	call	pthread_mutex_unlock
	cmpl	$99, %ebx
	jle	.L9
	movl	$0, %eax
	popq	%rbx
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE28:
	.size	one, .-one
	.globl	main
	.type	main, @function
main:
.LFB29:
	.cfi_startproc
	subq	$24, %rsp
	.cfi_def_cfa_offset 32
	movl	$0, %esi
	movl	$mtx, %edi
	call	pthread_mutex_init
	movl	$0, %ecx
	movl	$zero, %edx
	movl	$0, %esi
	movq	%rsp, %rdi
	call	pthread_create
	movl	$0, %ecx
	movl	$one, %edx
	movl	$0, %esi
	leaq	8(%rsp), %rdi
	call	pthread_create
	movl	$0, %esi
	movq	(%rsp), %rdi
	call	pthread_join
	movl	$0, %esi
	movq	8(%rsp), %rdi
	call	pthread_join
	movl	$mtx, %edi
	call	pthread_mutex_destroy
	movl	$0, %eax
	addq	$24, %rsp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE29:
	.size	main, .-main
	.globl	turn
	.bss
	.align 4
	.type	turn, @object
	.size	turn, 4
turn:
	.zero	4
	.comm	mtx,40,32
	.ident	"GCC: (Ubuntu 4.8.2-19ubuntu1) 4.8.2"
	.section	.note.GNU-stack,"",@progbits
