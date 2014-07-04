% ECMEL KAYTAZOÐLU 10060296
% SÜMEYRA ÖZGÜR 10060288
% MÝNE ÖZTÜRK 10060293

% HSV RENK UZAYI KULLANILARAK YAPILMIÞ YÜZ TANIMA PROGRAMI

fileFolder = fullfile(matlabroot,'faceDB');
DIR = dir(fullfile(fileFolder,'*.jpg'));
fileNames = {DIR.name}'
for fd=1:length(fileNames)
    im=imread(fileNames{fd});
    img=imresize(im, [400,400], 'bicubic'); %Resimleri yeniden boyutlandýrdýk
    imgend=img;  %Resmin çýktýsýnda kullanmak için kopya alýyoruz
    im = imadjust(img,stretchlim(img),[]);   % resme strech iþlemi uyguluyoruz
    hsv=rgb2hsv(im);    %rgb resmi hsv uzayýna dönüþtürüyoruz
    h=hsv(:,:,1);       %hsv'nin h sabitini alýyoruz
    s=hsv(:,:,2);       %hsv'nin s sabitini alýyoruz

    [r c v]=find(h>0.35 | s>=0.55 ); %cilt rengi dýþýnda kalan renk aralýðý
    numid=size(r,1);                 %döngü için boyut belirliyoruz
   
    for i=1:numid            
        img(r(i),c(i),:)=0;    %cilt rengi dýþýnda kalan renklerin hepsini 0 yapýyoruz
    end

    [r c v]=find(h>0.16 | s<=0.13 | s>0.7); %cilt rengi dýþýnda kalan renk aralýðý
    numid=size(r,1);                        
   
    for i=1:numid
        img(r(i),c(i),:)=0;    % üstteki döngü ile ayný ancak daha iyi bir sonuç vermesi açýsýndan farklý aralýklar alýndý
    end

    t=graythresh(img);  %Resmin thresh'ini alýyoruz
    bw=im2bw(img,t);    %Resmi bw'ye çeviriyoruz
    s=strel('disk',2);  %Resmi küçültmek için parametre alýyoruz
    bw=imerode(bw,s);   %Resimdeki nesneleri törpülüyoruz
    bw=bwareaopen(bw,800);  %800 deðerinden küçük nesneleri siliyoruz
    s=strel('disk',8);   %Resimdeki nesneleri büyültmek için parametre alýyoruz
    bw=imdilate(bw,s);   %Resimdeki nesnekeri büyültüyoruz
    bw=imfill(bw,'hole'); %Resimdeki boþluklarý dolduruyoruz

    [labeled,numObjects] = bwlabel(bw,4);%Alanlar etiketleniyor ve “numObjects” de ise kaç tane alan olduðu tutuluyor
    stats = regionprops(labeled,'Area','BoundingBox'); %BoundingBox þekillerin etrafýný çevirmeye yönelik bir özelliktir.

    areas = [stats.Area]; %Tüm alanlar ise areas atanýr.
    a=stats(1).Area; %herhangi bir alan atamasý yapýlýyor
    for n=2:numObjects %En büyük alaný bulunuyor
        max=stats(n).Area();
        if a<max
            a=max;
        end
    end

    imshow(imgend);

    idxOfDefects = find(areas == a ); %max alaný idxOfDefects deðiþkenine atadýk
    statsDefects = stats(idxOfDefects);

    hold on;
    for idx = 1 : length(statsDefects) %Çerveve çizimi
        h = rectangle('Position',statsDefects(idx).BoundingBox,'LineWidth',2); %pozisyonu ve çerçevenin kalýnlýðý belirlenir
        set(h,'EdgeColor',[.75 0 0]);
        hold on;
    end
    hold off;
    figure(fd)
end