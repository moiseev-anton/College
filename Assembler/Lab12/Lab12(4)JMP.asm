;������� �����
;��� 12
;������� 4 (JMP)
org 100h
begin:

voskl:
mov cx,10   ; ������ ������� �� 10 ��������
mov dx,'!'  ; ������ '!' � dx
mov ah, 2

print:
int 21h
dec cx
jz ex      ; ����� �� ����� 
jmp print  ; ����������� ������� �� print

ex:
inc bl
cmp bl,2
je ex1       ; ����� ������� ���� ������� �� ex:
 
mov ah, 9    ;����� hello
mov dx,offset msg   
int 21h   

jmp voskl


ex1:
ret
msg db "Hello$"      
end begin






