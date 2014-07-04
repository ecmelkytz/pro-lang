clc
b=imread('erode.png');
a=im2bw(b);
eski=im2bw(b);
[x,y]=size(a);
s=[[0 1 0];[1 1 1];[0 1 0]];
say=0;

for i=1:x-1
    for j=1:y-1
        if eski(i,j)==1
            say=say+1;
            a(i,j)=s(2,2)||a(i,j);
            a(i-1,j)=s(1,2)||a(i-1,j);
            a(i+1,j)=s(3,2)||a(i+1,j);
            a(i,j-1)=s(2,1)||a(i,j-1);
            a(i,j+1)=s(2,3)||a(i,j+1);
            a(i-1,j-1)=s(1,1)||a(i-1,j-1);
            a(i-1,j+1)=s(1,3)||a(i-1,j+1);
            a(i+1,j-1)=s(3,1)||a(i+1,j-1);
            a(i+1,j+1)=s(3,3)||a(i+1,j+1);
        end
    end
end

label=bwlabel(eski);
L1=label==1;
oz=regionprops(L1,'Area');
alan=oz.Area()

label=bwlabel(a);
L2=label==1;
oz=regionprops(L2,'Area');
alan2=oz.Area()
subplot(1,2,1);
imshow(b);
subplot(1,2,2);
imshow(a);
