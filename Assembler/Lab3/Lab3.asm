sseg    segment para stack 'stack'
        db 1,23,4,5,6,7,8,9,128 dup(0Ah)
sseg    ends

dseg    segment para public 'data'
b_tab   db 1ah,2bh,3ch,4dh,5eh,6fh,7ah,8bh
w_tab   dw 1a2bh,3c4dh,5e6fh,7a8bh
b_tab1  db 0ah,8 dup(1)
w_tab1  dw 8 dup(1)
dseg    ends  

eseg    segment
w_tab2  dw  11h,12h,13h,14h,15h,16h,17h,18h
eseg    ends

cseg    segment para public 'code'
prog    proc far
        assume  ds:dseg,cs:cseg,ss:sseg,es:eseg
        push ds
        mov ax,0
        push ax
        
        mov ax,dseg
        mov ds,ax
        mov ax,eseg
        mov es,ax
        
        mov al,-3
        mov ax,3
        mov b_tab,-3
        mov w_tab,-3
        mov ax,2a1bh 
        
        mov bl,al
        mov bh,al
        sub ax,bx
        sub ax,ax 
        
        mov ax,w_tab
        mov ax,w_tab+3
        mov ax,w_tab+5
        mov al,byte ptr w_tab+6
        mov al,b_tab
        mov al,b_tab+2
        mov ax,word ptr b_tab
        mov es:w_tab2+4,ax 
        
        mov bx,offset b_tab
        mov si,offset b_tab+1
        mov di,offset b_tab+2
        mov dl,[bx]
        mov dl,[si] 
        mov dl,[di]
        mov ax,[di]
        mov bp,bx
        mov al,[bp]
        mov al,ds:[bp]
        mov al,es:[bx]
        mov ax,cs:[bx]
        
        mov ax,[bx]+2
        mov ax,[bx]+4
        mov ax,[bx+2]
        mov ax,[4+bx] 
        mov ax,2+[bx]
        mov ax,4+[bx]
        mov al,[bx]+2
        mov bp,bx
        mov ax,[bp+2]
        mov ax,ds:[bp]+2
        mov ax,ss:[bx+2]
        
        mov si,2
        mov ah,b_tab[si]
        mov al,[b_tab+si]
        mov bh,[si+b_tab]
        mov bl,[si]+b_tab
        mov bx,es:w_tab2[si]
        mov di,4
        mov bl,byte ptr es:w_tab2[di]
        mov bl,b_tab[si]
        
        mov bx, offset b_tab
        mov al,3[bx][si]
        mov ah,[bx+3][si]
        mov al,[bx][si+2]
        mov ah,[bx+si+2]
        mov bp,bx
        mov ah,3[bp][si]
        mov ax,ds:3[bp][si]
        mov ax,word ptr ds:2[bp][si]
        ret
prog endp
cseg ends
end prog