;Moiseev Anton
;Lab8 Пример 1.2
org 100h
begin: 
mov ah,40h
mov bx,2  
mov dx, offset message
mov cx,25
int 21h
ret
message db "This function can print$"
end begin




