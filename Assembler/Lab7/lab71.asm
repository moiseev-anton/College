;LAB7 Variant3  Moiseev Anton
;X=(A*2+B*C)/(D-3)
;A=20 B=4 C=15 D=6
.model small
.stack 100h
.data
a db ?
b db ?
c db ?
d db ?
x dw ?
.code
start:
mov ax,@data
mov ds,ax
mov a,20 ;a=20
mov b,4  ;b=4
mov c,15 ;c=15
mov d,6  ;d=6
mov al,2
mul a    ;2*a=2*20=40
mov cx,ax
mov al,b
mul c    ;b*c=15*4=60
add ax,cx;40+60=100
mov cl,d
sub cl,3 ;d-3=6-3=3
div cl   ;100/3=33(1)
mov x,ax
mov ah,4ch
int 21h
end start
