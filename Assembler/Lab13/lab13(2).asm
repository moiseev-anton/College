;BX сумма повтор€ющихс€ элементов обоих массивов 
;dh сумма повтор€ющихс€ элементов обоих массивов
.model tiny
.stack 100h
.data 
ArrayA db 'moiseev'
ArrayB db 'anton'
NuMofEqual db 0; 
sum dw 0;


.code
start:
    mov si,offset ArrayA ;в si помещаем адрес 1 элемента массива ј 
    mov di,offset ArrayB ;в di помещаем адрес 1 элемента массива B 
    mov cx,7 ;устанавливаем число итераций цилка C1

C1:  
    push cx    ;сохран€ем в стек число оставшихс€ итераций цилка C1 дл€ передачи регистра cx циклу C2
    mov cx,5   ;устанавливаем число итераций цилка C2
    mov al,[si];помещаем в al элемент ArrayA[si]
 
C2:
    mov ah,[di] ;помещаем в ah элемент ArrayB[di]
    cmp al,ah   ;провер€ем равны ли они
    jnz end_C2
    mov cl,ah   ;если равны
    add cl,ah   ;считаем сумму
    add bx, cx  ;аккумулируем сумму
    inc dh      ;счетчик +1
    jmp EX_C2:  ;выходим из цикла C2

end_C2:     ;если не равны
    inc di  ;di++
    loop C2 ;переходим к следующей итерации C2 (cx--)
    
EX_C2:  
    pop cx ;возвращаем счетчик итераций цикла C1 из стека 
    inc si ;si++
    mov di,offset ArrayB ; возвращаем в di помещаем адрес 1 элемента массива B
    loop C1 ;переходим к следующей итерации C1 (cx--)
    
    mov NuMofEqual,dh ;результаты сохран€ем в переменных
    mov sum,bx
    
end start
