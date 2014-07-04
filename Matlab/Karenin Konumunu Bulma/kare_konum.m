clear all; 
clc;
im=imread('sol.png');
t=graythresh(im);
im=im2bw(im,t);

[x,y]=size(im);
sol=im(1:x,1:y/2);
sag=im(1:x,y/2+1:y);

alan=regionprops(im,'area');

if(sum(sol(:))< sum(sag(:))) && alan(1).Area<20000
    komut='uzakta saga git';
end
if(sum(sol(:))< sum(sag(:))) && alan(1).Area>20000
    komut='yakýnda saga git';
end
if(sum(sol(:))> sum(sag(:))) && alan(1).Area<20000
    komut='uzakta sola git';
end
if(sum(sol(:))> sum(sag(:))) && alan(1).Area>20000
    komut='yakýnda sola git';
end

if(sum(sol(:))== sum(sag(:))) && alan(1).Area>20000
    komut='yakýnda duz git';
end

imshow(im)
title(komut);