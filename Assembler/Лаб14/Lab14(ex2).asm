;������� �����
;��� �14
;������ 2
org 100h

    mov bx,3
    mov cx,10
next:
    inc bx
    loopnz next

ret

