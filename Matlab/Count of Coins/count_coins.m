
    img = imread('geld.tif');
   
    bw = im2bw(img,0);  %gri seviyeli resimlerde negatiflik alir

    bw = bwareaopen(bw,100);  % 30pixelden kucuk olanlar kaldiriliyor.
    SE =strel('disk', 7);
    bw2 = imerode(bw,SE);
    [L,num] = bwlabel(bw2);  %num ile para adetini ogrendik ve etiket atadik
    stats = regionprops(bw2, 'Area');
    
    [x,y]=size(bw);
    resimbuyuk=zeros(x,y);
    resimkucuk=zeros(x,y);
    big=zeros(x,y);
    
    for n=1:num
        l=L==n;
        a = stats(n).Area;
        if a>300
            big=big+l;
        elseif a>200 || a<300
            resimbuyuk=resimbuyuk+l;       
        else 
            resimkucuk=resimkucuk+l;
        end    
    end
    sx =strel('disk', 3);
    sy = imerode(resimbuyuk,sx);
    
    xbig=strel('disk', 6);
    ybig=imerode(big,xbig);
    
    yeni_resim=sy+ybig;
    
    [l,num]=bwlabel(yeni_resim);
    stats_yeni = regionprops(yeni_resim, 'Area');
    say=0;
    for n=1:num       
        say=say+1;
    end
    
   imshow(img);
   title(['Toplam para sayýsý = ',num2str(say)])

