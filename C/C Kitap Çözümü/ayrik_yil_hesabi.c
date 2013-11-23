/*Ayrık yıl hesabı*/

#include<stdio.h>
#include<conio.h>

int main(void)
{
    int yil;
    printf("yil giriniz:");
    scanf("%d",&yil);
    if(yil%4==0)
         
          if((yil%100==0) && (yil%400==0))
          printf("%d yili artik yildir.",yil);
          else if((yil%100!=0) && (yil%400!=0))
          printf("%d yili artik yildir.",yil);
          else
          printf("%d yili artik yil degildir.",yil);
    else if(yil%4!=0)
        printf("%d yili artik yil degildir.",yil);
    
    getch();
    return 0;
}    
