;Moiseev Anton
;Lab9 Variant 13
;(BH*(AH/13)/BL)    
; AH=30, BL=4, BH=4

org 100h

mov ah,30  ;ah=15
mov dl,13  ;dl=13 
mov bl,4   ;bl=4
mov bh,4   ;bh=4
mov al,ah  ;al=ah
xor ah,ah  ;ah=0
div dl     ;al=al/dl=30/13=2(4)
mul bh     ;al=al*bh=2*4=8
div bl     ;al=al/bl=8/4=2

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
mov ax,4c00h
int 21h
ret










