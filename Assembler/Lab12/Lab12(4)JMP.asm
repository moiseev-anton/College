;Моисеев Антон
;Лаб 12
;Задание 4 (JMP)
org 100h
begin:

voskl:
mov cx,10   ; ставим счетчик на 10 итераций
mov dx,'!'  ; символ '!' в dx
mov ah, 2

print:
int 21h
dec cx
jz ex      ; выход из цикла 
jmp print  ; безусловный переход на print

ex:
inc bl
cmp bl,2
je ex1       ; после второго раза переход на ex:
 
mov ah, 9    ;вывод hello
mov dx,offset msg   
int 21h   

jmp voskl


ex1:
ret
msg db "Hello$"      
end begin






