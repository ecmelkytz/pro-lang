/*ogrenci numara ve notunu girdi olarak alarak hangi nolu ogrencinin en yüksek puanı ve hangi nolu ogrencinin en dusuk puan aldigini hesaplama*/

#include<stdio.h>
#include<conio.h>
int main(void)
{
    int mevcut,no,not,dizino[100],dizinot[100],i,max=0,min=100,siramax,siramin;
    printf("Sinif mevcudunu giriniz:");
    scanf("%d",&mevcut);
    for(i=0;i<mevcut;i++)
    {
        printf("ogrenci numarasini ve notunu giriniz:");                 
        scanf("%d %d",&dizino[i],&dizinot[i]);
    }
    /*puan icin*/
    for(i=1;i<mevcut;i++)
    {
        if(dizinot[i]>max)
        {
            max=dizinot[i];
            siramax=i;
        }
        if(dizinot[i]<min)
        {
            min=dizinot[i];
            siramin=i;
        }
    }               
    printf("\n%d numarali ogrenci en yuksek notu (%d) almistir.",dizino[siramax],max);
    printf("\n%d numarali ogrensi en dusuk notu (%d) almistir.",dizino[siramin],min);
    getch();
    return 0;       
}
