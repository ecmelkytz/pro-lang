clc;
im=imread('para.png');
t=graythresh(im);
resim=imcomplement(im2bw(im,t));
resim=imfill(resim,'hole');
s=strel('disk',50);
r=imerode(resim,s);
a=regionprops(r,'area')

bir=0;
ellikurus=0;
yirmibeskurus=0;
onkurus=0;
beskurus=0;

for i=1:length(a)
    if a(i).Area>35000
        bir=bir+1;
    elseif a(i).Area>25000 && a(i).Area<35000
        ellikurus=ellikurus+0.5;
    elseif a(i).Area>15000 && a(i).Area<20000
        yirmibeskurus=yirmibeskurus+0.25;
    elseif a(i).Area>11000 && a(i).Area<13000
        onkurus=onkurus+0.1;
    else
        beskurus=beskurus+0.05;
    end
end

toplam=bir+ellikurus+yirmibeskurus+onkurus+beskurus;
imshow(im);
title(['Para Miktari = ',num2str(toplam),' TL']);

