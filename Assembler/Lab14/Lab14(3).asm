;������� �����
;��� �14
;������� 3
org 100h
start:
    mov ah,09h      ;������������� ������� 09h (����� ������) � ������� ah
    lea dx,string   ; �������� ����� ������ string � dx
    int 21h         ; ����� 21h ���������� ��� ������
mm:
    cld              ; ������� ���� �����������
    mov al,'l'       ; �������� 'l' � al (�����, ������� ����)
    lea di,string    ; �������� ����� ������ � di
    mov cx,27        ; ������������� cx �� 27 (����� ������)
    repne scasb      ; ���� 'l' � ������, �������� ������
    ;repne - repit while not equel
    ;scasb - ���������� al c ��������� ������ �� ������� ��������� di
    dec di           ; di--
    
    jcxz exit        ; ���� cx ����� ���� (����� 'l' �� �������), ������� � exit
    mov bx,26       ; ��������� 26 (����� ������ - 1) � bx
    sub bx,cx        ; bx = 26 - cx (������� ������� ����� 'l' �� ����� ������)
    mov al,string[bx]; �������� � al ������, ����������� � ������� 'bx'
    
    add kol,1        ; kol = kol + 1
    xor al,al        ; �������� al
    mov string[bx],al; �������� ������ � ������� 'bx' �� ���� (������� ��� �� ������)
    jmp mm           ;������� � mm

exit:
   mov dl,al   ;����� ������� �����
   mov ah,02h
   int 21h
   add kol,48
   mov al,kol  ;����� ����������
   mov dl,al
   mov ah,02h
   int 21h
   
    mov ah,4h
    int 21h   
    
    string db 'hello, aaworldASTRING perl',0ah, 0dh,'$'
    kol db 0
end start

ret