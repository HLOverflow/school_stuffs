section .text

global _start

_start:
	;push 0x00000000
	xor eax, eax
	push eax

	;push hs/nib//
	push 0x68732f6e
	push 0x69622f2f

	;make ebx point to top of stack
	mov ebx, esp
	
	;put edb address of 0x00000000
	push eax
	mov edx, esp

	;ecx need address of hs/nib//
	push ebx
	mov ecx, esp

	;execve is sys call number 11
	mov al, 11
	
	;call kernel
	int 0x80


