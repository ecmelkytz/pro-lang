clc;
a=imread('cameraman.tif');
 
t=[2 0 0; 0 3 0; 0 0 1];
 
tform=maketform('affine',t);
k=imtransform(a,tform);
figure(1);
imshow(a); title('Orjinal Resim');
figure(2);
imshow(k); title('Affine Uygulandý');
 
kose=diag(t);
z=[1 0 0; 0 1 0; 0 0 1];
 
for i=1:length(z)
    z(1,i)=z(1,i)/kose(1);
    z(2,i)=z(2,i)/kose(2);
end
 
yeni=maketform('affine',z)
yeni=imtransform(k,yeni);
figure(3);
imshow(yeni); title('Resim Eski Haline Getirildi');