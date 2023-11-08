;Moiseev Anton
;Lab8 Пример 3.1 
org 100h
begin:
mov ax,0003h
int 10h
mov ax,0B800h
mov es,ax
mov di,0
mov ah,31
mov al,65 ;'A'
mov es:[di],ax
mov ah,10h
int 16h

ret
end begin

