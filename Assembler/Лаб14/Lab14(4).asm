;������� �����
;��� �14
;������� 4
org 100h
.data
res db 0ah, 0dh, 'result = ','$'
noz db 0ah, 0dh, 'No zero','$'
msg db 0ah, 0dh, 'Array-','$'
mas db 1,2,0,4,5,6
i db 0
.code
    
    mov ah, 09h      ;����� 'Array-'
    lea dx,msg
    int 21h
    
    mov cx, 6        ; ������������� ����� �������� ����� (����� �������)
    mov si,0         ; ������������� ������ si � 0
    mov ah,02h       ; ������������� ������� 09h (����� �������) � ������� ah
    
show:
    mov dl,mas[si]   ; �������� ������� ������� � dl
    add dl,30h       ; �������� �������� dl �� ASCII (���������� � '0')
    int 21h          ; ����� 21h ���������� ��� ������
    inc si           ;si++
    loop show        ; ������� �� ����� show
    
    mov cx, 6        ; ������������� ����� �������� ����� (����� �������)
    mov si,0         ; ������������� ������ si � 0
    xor bh,bh        ; ���������� ������ si � 0 (������ �������)
find_zero:
    mov al, mas[si]  ; �������� ������� ������� ������� � ������� al
    cmp al, 0        ; ���������� ��� � �����
    je zero_found    ; ���� ����� ����, ������� �� ����� �� ����� zero_found
    inc si
    inc bh           ; ����� ����������� ������
    loop find_zero   ; ��������� �� ����� find_zero: (cx--)
zero_found:
    
    mov ah, 09h
    cmp cx,0         ; �������� ���� cx=0 ������ � ������� ��� 0
    jne result
    
    lea dx,noz       ; ����� 'No zero'
    int 21h
    jmp exit

result:              ; �����
    lea dx,res       ; ����� 'result = '
    int 21h
    mov ah,02h       ; ����� ���������� (����� �������� ������� 0)
    mov dl,bh
    add dl,30h
    int 21h    
    
    
exit:    
    mov ah,4ch
    int 21h