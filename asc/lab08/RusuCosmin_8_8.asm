;Rusu Cosmin - gr. 917, 26.11.2015, homework for lab08, problem 08

;8. Write a program which reads the name of a file and two characters from the keyboard. 
;The program should replace all occurrences of the first character in that file with the 
;second character given by the user.

assume cs:code, ds:data

data segment
	

data ends


code segment
start:
	mov ax, data
	mov dx, ax

	mov ax, 4c00h
	int 21h
code ends
end start
