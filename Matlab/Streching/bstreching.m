clc; clear all;
im =double( imread('pout.tif'));
s=size(im);
son = zeros(s(1),s(2));
a=min(im(:));
b=max(im(:));
im = (im > a).* im;
im = (im >= b)*255+(im<b).*im;
son = uint8(255*(a-im)/(a-b));

subplot(1,2,1);imshow('pout.tif');
subplot(1,2,2);imshow(son);

