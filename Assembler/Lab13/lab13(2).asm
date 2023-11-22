;BX ����� ������������� ��������� ����� �������� 
;dh ����� ������������� ��������� ����� ��������
.model tiny
.stack 100h
.data 
ArrayA db 'moiseev'
ArrayB db 'anton'
NuMofEqual db 0; 
sum dw 0;


.code
start:
    mov si,offset ArrayA ;� si �������� ����� 1 �������� ������� � 
    mov di,offset ArrayB ;� di �������� ����� 1 �������� ������� B 
    mov cx,7 ;������������� ����� �������� ����� C1

C1:  
    push cx    ;��������� � ���� ����� ���������� �������� ����� C1 ��� �������� �������� cx ����� C2
    mov cx,5   ;������������� ����� �������� ����� C2
    mov al,[si];�������� � al ������� ArrayA[si]
 
C2:
    mov ah,[di] ;�������� � ah ������� ArrayB[di]
    cmp al,ah   ;��������� ����� �� ���
    jnz end_C2
    mov cl,ah   ;���� �����
    add cl,ah   ;������� �����
    add bx, cx  ;������������ �����
    inc dh      ;������� +1
    jmp EX_C2:  ;������� �� ����� C2

end_C2:     ;���� �� �����
    inc di  ;di++
    loop C2 ;��������� � ��������� �������� C2 (cx--)
    
EX_C2:  
    pop cx ;���������� ������� �������� ����� C1 �� ����� 
    inc si ;si++
    mov di,offset ArrayB ; ���������� � di �������� ����� 1 �������� ������� B
    loop C1 ;��������� � ��������� �������� C1 (cx--)
    
    mov NuMofEqual,dh ;���������� ��������� � ����������
    mov sum,bx
    
end start
