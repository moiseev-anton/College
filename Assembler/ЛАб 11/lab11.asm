;Моисеев Антон
;Лаб 11
;Пример

.data
a db ?
x db ?
y db ?
y2 db ?
per db 10,13,'$'
mesa db 10,13,'Input a:$'
mesx db 10,13,'Input x:$',10,13
.stack
db 128 dup(?)

.code
main:
assume ss:s,ds:data,cs:code
mov ax,data
mov ds,ax
mov dx,offset mesa

mov ah,9 ;приглашение на ввод a
int 21h

mov ah,1 ;считывание нажатого символа
int 21h                              
sub al,30h
mov a,al ;запись считанного в переменную а

mov dx, offset mesx
mov ah,9  ;приглдашение на ввод x
int 21h

  
mov ah,1  
int 21h
sub al,30h
mov x,al   ;запись считанного в переменную x

mov dx,offset per   ;Перевод строки
mov ah,9  
int 21h

mov al,x
xor ah,ah
mov dl,3
div dl
cmp ah,1    
je equal   ;если x mod 3=1 то перейти на метку equal:
notequal:   
add al,7
mov y2,7   ;у2=7

jmp l1

equal:     
mov al,x
add al,a
mov y2,al   ;у2=х+а



l1:
mov al,x
cmp al,0
jl lower   ;если х<0 то перейти на метку lower, иначе higher
higher:
sub al,a    ; y1=x-а
sub al,y2
mov y,al    ;у = у1 - у2

jmp short l2

lower:
neg al      ; y1=|x|
sub al,y2    
mov y,al    ;у = у1 - у2

l2:
test al,al
jns positive   ;если у положительный переход к метке positive
negative:
neg al         ;меняем на число с противополодным знаком
mov y,al

mov ah, 2h     ;печать минуса
mov dl, '-'    
int 21h

 
positive: 
mov ah,0   ;Вывод y
mov al,y
push -1
mov cx,10
l3:
mov dx,0
div cx
push dx
cmp ax,0
jne l3
mov ah,2h
l4:
pop dx
cmp dx,-1
je ex
add dl, '0'
int 21h
jmp l4
ex:

mov ah,0;Ожидание нажатия клавиши
int 16h

mov ah,4ch
int 21h

end main