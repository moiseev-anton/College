;Moiseev Anton
;Lab9 Variant 13
;(AL*40)/(BH*AH)    
; AL=2,BL=3,AH=4,BH=5

org 100h

xor ax,ax ;очистка ax
mov al,2  ;al=2
mov dl,40 ;dl=40
mul dl    ;al=al*dl=2*40=80
mov dl,al ;dl=al=80
mov bh,5  ;bh=5
mov al,4  ;al=4
mul bh    ;al=al*bh=4*5=20
mov dh,al ;dh=al=20
mov al,dl ;al=dl=80
div dh    ;al=al/dh=80/20=4

mov bx,0
mov bx,ax ;сохраняем результат

start:      ;вывод результата
mov ax, bx
push -1
mov cx,10  

l:
mov dx,0
div cx
push dx
cmp ax,0
jne l
mov ah,2h

l2:
pop dx
cmp dx,-1
je ex
add dl,'0'
int 21h
jmp l2

ex:
mov ax,4c00h
int 21h
ret




