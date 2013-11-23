/*Fahrenheit Celsius dönüşümü*/

#include<stdio.h>
#include<conio.h>


int c(int);
int f(int);
int main(void)
{
    char k,enter;
    int deger,sonuc;
    printf("Fahrenheit-->Celsius icin C/c\n");
    printf("Celsius-->Fahrenheit icin F/f\n");
    printf("seciminizi giriniz:");
    scanf("%c",&k);
    if(k=='c' || k=='C')
    {
          printf("Fahrenheit degerini giriniz:");
          scanf("%d",&deger);
          printf("celsius degeri:%d",c(deger));
    }
    else if(k=='f' || k=='F')
    {
         printf("celsius degerini giriniz:");
         scanf("%d",&deger);
         printf("fahrenheit degeri:%d",f(deger));
    }
    getch();
    return 0;    
}
int c(int fah)  
{
    int islem;
    islem=(5*fah-160)/9;

}
int f(int cel)
{
    int islem;
    islem=(9*cel+160)/5;
    
}
    

