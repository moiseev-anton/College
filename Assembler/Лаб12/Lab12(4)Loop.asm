;Моисеев Антон
;Лаб 12
;Задание 4 (Loop)
org 100h
begin:

voskl:
mov cx,10   ; ставим счетчик на 10 итераций
mov dx,'!'  ; символ '!' в dx
mov ah, 2

print:
int 21h      ; Вызов прерывания 
loop print  ; уменьшаем cx и выполняем пока cx > 0

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
