;ћоисеев јнтон
;Ћаб є14
;«адание 4
org 100h
.data
res db 0ah, 0dh, 'result = ','$'
noz db 0ah, 0dh, 'No zero','$'
msg db 0ah, 0dh, 'Array-','$'
mas db 1,2,0,4,5,6
i db 0
.code
    
    mov ah, 09h      ;вывод 'Array-'
    lea dx,msg
    int 21h
    
    mov cx, 6        ; устанавливаем число итераций цикла (длина массива)
    mov si,0         ; устанавливаем индекс si в 0
    mov ah,02h       ; установливаем функцию 09h (вывод символа) в регистр ah
    
show:
    mov dl,mas[si]   ; помещаем текущий элемент в dl
    add dl,30h       ; смещение значени€ dl по ASCII (добавление к '0')
    int 21h          ; вызов 21h прерывани€ дл€ вывода
    inc si           ;si++
    loop show        ; переход на метку show
    
    mov cx, 6        ; устанавливаем число итераций цикла (длина массива)
    mov si,0         ; устанавливаем индекс si в 0
    xor bh,bh        ; сбрасываем индекс si в 0 (начало массива)
find_zero:
    mov al, mas[si]  ; помещаем текущий элемент массива в регистр al
    cmp al, 0        ; сравниваем его с нулем
    je zero_found    ; если равен нулю, выходим из цикла на метку zero_found
    inc si
    inc bh           ; иначе увеличиваем индекс
    loop find_zero   ; переходим на метку find_zero: (cx--)
zero_found:
    
    mov ah, 09h
    cmp cx,0         ; проверка если cx=0 значит в массиве нет 0
    jne result
    
    lea dx,noz       ; вывод 'No zero'
    int 21h
    jmp exit

result:              ; иначе
    lea dx,res       ; вывод 'result = '
    int 21h
    mov ah,02h       ; вывод результата (номер элемента равного 0)
    mov dl,bh
    add dl,30h
    int 21h    
    
    
exit:    
    mov ah,4ch
    int 21h