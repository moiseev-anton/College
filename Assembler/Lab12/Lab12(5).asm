;������� �����
;��� 12
;������� 5


org 100h
begin:
mov cx,14 ;������ ������� �� 14 ��������
sum:
add ax,cx ;
loop sum  ;��������� cx � ��������� ���� cx > 0
ret    
end begin      




