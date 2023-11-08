;Моисеев Антон
;Лаб 12
;Задание 4 (JNZ)
org 100h
begin:

voskl:
mov cx,10   ; ставим счетчик на 10 итераций
mov dx,'!'  ; символ '!' в dx
mov ah, 2

print:
int 21h    ; Вызов прерывания
dec cx     ;уменьшаем cx
jnz print  ; пока cx не 0 переход на print

inc bl
cmp bl,2
je ex       ; после второго раза переход на ex:


mov ah, 9    ;вывод hello
mov dx,offset msg   
int 21h   

jmp voskl


ex:
ret
msg db "Hello$"      
end begin



