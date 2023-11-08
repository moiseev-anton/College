;Moiseev Anton
;Lab8 Hello 
org 100h

begin:

mov ah,09
mov dx,offset mes
int 21h

mes db "Hello$"
ret

end begin



