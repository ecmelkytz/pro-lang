function gammaCorrection(name, c, gamma)
 name='cameraman.tif';
 c=1;
 gamma=2;
 r = imread (name);
 r=im2double(r);
 s = c * (r .^ gamma);
 subplot (1 ,2 ,1)
 imshow(r);

 title('Original');
 subplot (1 ,2 ,2)
 imshow(s)

 title(sprintf('Gamma: %0.1f',gamma));
end