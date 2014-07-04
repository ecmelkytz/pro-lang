clc
b=imread('dilat.png');
a=im2bw(b);
eski=im2bw(b);
[x,y]=size(a);
s=[1; 1; 1];
say=0;

for i=2:x-1
    for j=2:y-1
        if eski(i,j)==1
            if ((s(2,1)||a(i,j))&&(s(1,1)||a(i-1,j)) && (s(3,1)||a(i+1,j)))~=1
            say=say+1;
            a(i,j)=1;

            end
        else
            a(i,j)=0;
            a(i-1,j)=0;
            a(i+1,j)=0;
        end
    end
end

label=bwlabel(eski);
L1=label==1;
oz=regionprops(L1,'Area');
alan=sum(L1(:))

label=bwlabel(a);
L2=label==1;
oz=regionprops(L2,'Area');
alan2=oz.Area()

subplot(1,2,1);
imshow(b);
subplot(1,2,2);
imshow(a);
