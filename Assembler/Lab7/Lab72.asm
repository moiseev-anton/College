;Lab7(2) Moiseev Anton
;10101101b   
.model tiny
.stack 100h
.code
start:
mov ah,10101101b ;al=10101101b  (173)
shr ah,1         ;al=01010110b (86)

mov ah,10101101b ;al=10101101b  (173)
shl ah,1         ;al=01011010b (90)              

mov ah,10101101b ;al=10101101b   (173)
sar ah,1         ;al=11010110b (214)  

mov ah,10101101b ;al=10101101b  (173)
ror ah,1         ;al=11010110 (214)  

mov ah,10101101b ;al=10101101b  (173)
rol ah,1         ;al=01011011b (91)  

mov ax,4c00h
int 21h
end start



