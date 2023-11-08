;ћоисеев јнтон
;Ћаб є14
;«адание 3
org 100h
start:
    mov ah,09h      ;установливаем функцию 09h (вывод строки) в регистр ah
    lea dx,string   ; помещаем адрес строки string в dx
    int 21h         ; вызов 21h прерывани€ дл€ вывода
mm:
    cld              ; очищаем флаг направлени€
    mov al,'l'       ; помещаем 'l' в al (букву, которую ищем)
    lea di,string    ; помещаем адрес строки в di
    mov cx,27        ; устанавливаем cx на 27 (длина строки)
    repne scasb      ; ищем 'l' в строке, двига€сь вперед
    ;repne - repit while not equel
    ;scasb - сравнивает al c элементом строки на который указывает di
    dec di           ; di--
    
    jcxz exit        ; если cx равен нулю (буква 'l' не найдена), перейти к exit
    mov bx,26       ; загружаем 26 (длина строки - 1) в bx
    sub bx,cx        ; bx = 26 - cx (находим позицию буквы 'l' от конца строки)
    mov al,string[bx]; помещаем в al символ, наход€щийс€ в позиции 'bx'
    
    add kol,1        ; kol = kol + 1
    xor al,al        ; обнул€ем al
    mov string[bx],al; замен€ем символ в позиции 'bx' на ноль (удал€ем его из строки)
    jmp mm           ;ѕереход к mm

exit:
   mov dl,al   ;вывод искомой буквы
   mov ah,02h
   int 21h
   add kol,48
   mov al,kol  ;вывод количества
   mov dl,al
   mov ah,02h
   int 21h
   
    mov ah,4h
    int 21h   
    
    string db 'hello, aaworldASTRING perl',0ah, 0dh,'$'
    kol db 0
end start

ret