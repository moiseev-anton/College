;������� �����
;��� 12
;������� 4 (JNZ)
org 100h
begin:

voskl:
mov cx,10   ; ������ ������� �� 10 ��������
mov dx,'!'  ; ������ '!' � dx
mov ah, 2

print:
int 21h    ; ����� ����������
dec cx     ;��������� cx
jnz print  ; ���� cx �� 0 ������� �� print

inc bl
cmp bl,2
je ex       ; ����� ������� ���� ������� �� ex:


mov ah, 9    ;����� hello
mov dx,offset msg   
int 21h   

jmp voskl


ex:
ret
msg db "Hello$"      
end begin



