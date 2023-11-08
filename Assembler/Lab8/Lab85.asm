;Moiseev Anton
;Lab8 Пример 2.3.1 
org 100h
begin:
mov ah,09
mov bh,0
mov al,65 ;'A'
mov bl,00011101b
mov cx,555
int 10h 
ret
end begin




