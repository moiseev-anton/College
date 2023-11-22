;BX сумма повтор€ющихс€ элементов обоих массивов 
;dh сумма повтор€ющихс€ элементов обоих массивов
.model tiny
.stack 100h
.data 
ArrayA db 05,10,06,44,20,32,05,11,46,0
ArrayB db 35,10,15,44,20,02,65,10,46,0
NuMofDiff dw 0 ;
NuMofEqual dw 0; 
sumO dw 0;
sumR dw 0;

.code
start:
    mov si,offset ArrayA ;в si помещаем адрес 1 элемента массива ј 
    mov di,offset ArrayB ;в di помещаем адрес 1 элемента массива B 
    mov cx,10 ;устанавливаем число итераций цилка loop C1

C1:  
    push cx    ;сохран€ем в стек число итераций цилка loop C1 дл€ передачи cx циклу C2
    mov cx,10  ;устанавливаем число итераций цилка C2
    mov al,[si];помещаем в al элемент ArrayA[si]
 
C2:
    mov ah,[di] ;помещаем в ah элемент ArrayB[di]
    cmp al,ah   ;провер€ем равны ли они
    jnz end_C2
    mov cl,ah   ;если равны
    add cl,ah
    add BX, cx  ;аккумулируем сумму
    inc DH      ;счетчик +1
    jmp EX_C2:  ;выходим из цикла C1

end_C2:     ;если не равны
    inc di  ;di++
    loop C2 ;переходим к следующей итерации (cx--)
    
EX_C2:  
    pop cx ;возвращаем счетчик итераций цикла C1 из стека 
    inc si ;si++
    mov di,offset ArrayB ; возвращаем в di помещаем адрес 1 элемента массива B
    loop C1 ;переходим к следующей итерации (cx--) 
end start
