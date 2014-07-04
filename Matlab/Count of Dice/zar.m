clc;
im=imread('zar.png');
resim=im;
t=graythresh(im);
im=im2bw(im,t);
 
say1=0;
say2=0;
 
l=bwlabel(im); 
x=regionprops(l,'area');

for i=2:length(x)
    if x(i).Area==bul  %Ayný boyuttaki iþaretleri topla
        say1=say1+1;
    elseif x(i).Area~=bul
        say2=say2+1;
    end
end
imshow(resim)
title(['Üste Gelen Sayý: ',num2str(say1)])