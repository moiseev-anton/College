;Moiseev Anton
;Lab9 Variant 13
;(13(#)*AL)/BL    
; AL=15,BL=4

org 100h

xor ax,ax ;очистка ax
mov al,15  ;al=15
mov dl,13  ;dl=13
mul dl    ;al=al*dl=15*13=195
mov bl,4  ;bl=4
div bl    ;al=al/bl=195/4=48(3)


mov bh,ah ;прячем остаток

mov ah,0


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

mov al,bh  ; вывод остатка
mov ah,0


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
je ex1
add dl,'0'
int 21h
jmp l4

ex1:
mov ax,4c00h
int 21h
ret






