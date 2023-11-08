;Moiseev Anton
;Lab8 Пример 2.2.1
org 100h
begin:
mov ah,02
mov bh,0
mov dh,12
mov dl,29
int 10h 
mov ax,65
int 29h
ret
end begin





