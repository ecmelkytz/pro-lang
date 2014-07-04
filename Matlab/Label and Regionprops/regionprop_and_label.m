clc;
im=imread('coins.png');
im=im2bw(im);
im=imfill(im,'hole');
subplot(2,2,1);
imshow(im);
title('BW Resim');

label=bwlabel(im);
toplam=max(max(label));
L1=label==1;
oz=regionprops(L1,'Area','Centroid','Boundingbox');
alan=oz(1).Area
merkez=oz(1).Centroid
kaplama=oz(1).BoundingBox
subplot(2,2,2);
imshow(L1); 
title('Seçilmiþ Label');

subplot(2,2,3);
imshow(im-L1);
title('Label Çýkarýlmýþ');
