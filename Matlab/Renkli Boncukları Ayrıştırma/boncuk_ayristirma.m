function boncuk_ayristirma(im)
    im = imread('http://i.imgur.com/TwDQZKO.jpg');
 
    subplot(3,2,1); imshow(sari(im)); title('Sarý Boncuklar');
    subplot(3,2,2); imshow(mavi(im)); title('Mavi Boncuklar');
    subplot(3,2,3); imshow(turuncu(im)); title('Turuncu Boncuklar');
    subplot(3,2,4); imshow(bordo(im)); title('Bordo Boncuklar');   
    subplot(3,2,5); imshow(siyah(im)); title('Siyah Boncuklar');
    subplot(3,2,6); imshow(yesil(im)); title('Yeþil Boncuklar');
end
 
function v = sari(im)
    r = im(:,:,1);
    g = im(:,:,2);
    b = im(:,:,3);
    bwr = r >= 200;
    bwg = g >= 185;
    bwb = b <= 60;
    bw = bwr .* bwg .* bwb;
    bw=imfill(bw,'hole');
    bw3 = cat(3,bw,bw,bw);
    v = uint8(double(im) .* bw3);  
end
 
function v = mavi(im)
    r = im(:,:,1);
    g = im(:,:,2);
    b = im(:,:,3);
    bwr = r <= 50;
    bwg = g <= 150;
    bwb = b >= 125;
    bw = bwr .* bwg .* bwb;
    bw=imfill(bw,'hole');
    bw3 = cat(3,bw,bw,bw);
    v = uint8(double(im) .* bw3);
 
end
 
function v = turuncu(im)
    r = im(:,:,1);
    g = im(:,:,2);
    b = im(:,:,3);
    bwr = r >= 220;
    bwg = g <= 130;
    bwb = b<= 55;
    bw = bwr .* bwg .* bwb;
    bw=imfill(bw,'hole');
    bw3 = cat(3,bw,bw,bw);
    v = uint8(double(im) .* bw3);
 
end
 
function v = bordo(im)
    r = im(:,:,1);
    g = im(:,:,2);
    b = im(:,:,3);
    bwr = r >= 140;
    bwg = g <= 50;
    bwb = b <= 120;
    bw = bwr .* bwg .* bwb;
    bw=imfill(bw,'hole');
    bw3 = cat(3,bw,bw,bw);
    v = uint8(double(im) .* bw3);
end
 
function v = siyah(im)
    r = im(:,:,1);
    g = im(:,:,2);
    b = im(:,:,3);
    bwr = r <= 80;
    bwg = g <= 70;
    bwb = b <= 55;
    bw = bwr .* bwg .* bwb;
    bw=imfill(bw,'hole');
    bw3 = cat(3,bw,bw,bw);
    v = uint8(double(im) .* bw3);  
end
 
function v = yesil(im)
    r = im(:,:,1);
    g = im(:,:,2);
    b = im(:,:,3);
    bwr = r <= 150;
    bwg = g >= 150;
    bwb = b <= 150;
    bw = bwr .* bwg .* bwb;
    bw=imfill(bw,'hole');
    bw3 = cat(3,bw,bw,bw);
    v = uint8(double(im) .* bw3);  
end