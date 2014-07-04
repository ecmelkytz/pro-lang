% ECMEL KAYTAZO�LU 10060296
% S�MEYRA �ZG�R 10060288
% M�NE �ZT�RK 10060293

% HSV RENK UZAYI KULLANILARAK YAPILMI� Y�Z TANIMA PROGRAMI

fileFolder = fullfile(matlabroot,'faceDB');
DIR = dir(fullfile(fileFolder,'*.jpg'));
fileNames = {DIR.name}'
for fd=1:length(fileNames)
    im=imread(fileNames{fd});
    img=imresize(im, [400,400], 'bicubic'); %Resimleri yeniden boyutland�rd�k
    imgend=img;  %Resmin ��kt�s�nda kullanmak i�in kopya al�yoruz
    im = imadjust(img,stretchlim(img),[]);   % resme strech i�lemi uyguluyoruz
    hsv=rgb2hsv(im);    %rgb resmi hsv uzay�na d�n��t�r�yoruz
    h=hsv(:,:,1);       %hsv'nin h sabitini al�yoruz
    s=hsv(:,:,2);       %hsv'nin s sabitini al�yoruz

    [r c v]=find(h>0.35 | s>=0.55 ); %cilt rengi d���nda kalan renk aral���
    numid=size(r,1);                 %d�ng� i�in boyut belirliyoruz
   
    for i=1:numid            
        img(r(i),c(i),:)=0;    %cilt rengi d���nda kalan renklerin hepsini 0 yap�yoruz
    end

    [r c v]=find(h>0.16 | s<=0.13 | s>0.7); %cilt rengi d���nda kalan renk aral���
    numid=size(r,1);                        
   
    for i=1:numid
        img(r(i),c(i),:)=0;    % �stteki d�ng� ile ayn� ancak daha iyi bir sonu� vermesi a��s�ndan farkl� aral�klar al�nd�
    end

    t=graythresh(img);  %Resmin thresh'ini al�yoruz
    bw=im2bw(img,t);    %Resmi bw'ye �eviriyoruz
    s=strel('disk',2);  %Resmi k���ltmek i�in parametre al�yoruz
    bw=imerode(bw,s);   %Resimdeki nesneleri t�rp�l�yoruz
    bw=bwareaopen(bw,800);  %800 de�erinden k���k nesneleri siliyoruz
    s=strel('disk',8);   %Resimdeki nesneleri b�y�ltmek i�in parametre al�yoruz
    bw=imdilate(bw,s);   %Resimdeki nesnekeri b�y�lt�yoruz
    bw=imfill(bw,'hole'); %Resimdeki bo�luklar� dolduruyoruz

    [labeled,numObjects] = bwlabel(bw,4);%Alanlar etiketleniyor ve �numObjects� de ise ka� tane alan oldu�u tutuluyor
    stats = regionprops(labeled,'Area','BoundingBox'); %BoundingBox �ekillerin etraf�n� �evirmeye y�nelik bir �zelliktir.

    areas = [stats.Area]; %T�m alanlar ise areas atan�r.
    a=stats(1).Area; %herhangi bir alan atamas� yap�l�yor
    for n=2:numObjects %En b�y�k alan� bulunuyor
        max=stats(n).Area();
        if a<max
            a=max;
        end
    end

    imshow(imgend);

    idxOfDefects = find(areas == a ); %max alan� idxOfDefects de�i�kenine atad�k
    statsDefects = stats(idxOfDefects);

    hold on;
    for idx = 1 : length(statsDefects) %�erveve �izimi
        h = rectangle('Position',statsDefects(idx).BoundingBox,'LineWidth',2); %pozisyonu ve �er�evenin kal�nl��� belirlenir
        set(h,'EdgeColor',[.75 0 0]);
        hold on;
    end
    hold off;
    figure(fd)
end