clc;
im=imread('cameraman.tif');
a=im(1:256,1:50);
b=im(1:256,50:99);
c=im(1:256,100:149);
d=im(1:256,150:199);
e=im(1:256,200:255);

a=histeq(a,2);
b=histeq(b,3);
c=histeq(c,4);
d=histeq(d,5);
e=histeq(e,6);

[x,y]=size(im);

resim=uint8(zeros(x,y));
resim(1:256,1:50)=a;
resim(1:256,50:99)=b;
resim(1:256,100:149)=c;
resim(1:256,150:199)=d;
resim(1:256,200:255)=e;

imshow(resim)
