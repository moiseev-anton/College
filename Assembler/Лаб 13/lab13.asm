;BX ����� ������������� ��������� ����� �������� 
;dh ����� ������������� ��������� ����� ��������
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
    mov si,offset ArrayA ;� si �������� ����� 1 �������� ������� � 
    mov di,offset ArrayB ;� di �������� ����� 1 �������� ������� B 
    mov cx,10 ;������������� ����� �������� ����� loop C1

C1:  
    push cx    ;��������� � ���� ����� �������� ����� loop C1 ��� �������� cx ����� C2
    mov cx,10  ;������������� ����� �������� ����� C2
    mov al,[si];�������� � al ������� ArrayA[si]
 
C2:
    mov ah,[di] ;�������� � ah ������� ArrayB[di]
    cmp al,ah   ;��������� ����� �� ���
    jnz end_C2
    mov cl,ah   ;���� �����
    add cl,ah
    add BX, cx  ;������������ �����
    inc DH      ;������� +1
    jmp EX_C2:  ;������� �� ����� C1

end_C2:     ;���� �� �����
    inc di  ;di++
    loop C2 ;��������� � ��������� �������� (cx--)
    
EX_C2:  
    pop cx ;���������� ������� �������� ����� C1 �� ����� 
    inc si ;si++
    mov di,offset ArrayB ; ���������� � di �������� ����� 1 �������� ������� B
    loop C1 ;��������� � ��������� �������� (cx--) 
end start
