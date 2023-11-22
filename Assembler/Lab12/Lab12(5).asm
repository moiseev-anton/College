;Моисеев Антон
;Лаб 12
;Задание 5


org 100h
begin:
mov cx,14 ;ставим счетчик на 14 итераций
sum:
add ax,cx ;
loop sum  ;уменьшаем cx и выполняем пока cx > 0
ret    
end begin      




