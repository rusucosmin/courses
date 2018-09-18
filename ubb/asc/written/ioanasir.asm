assume ds:data

data segment public
	sir db 1, 0, 1, 2, 0, 1, 2, 3, 0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 0
	ls dw $ - sir
data ends
public sir
public ls

end
