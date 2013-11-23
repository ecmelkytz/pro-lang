/*Mutlak deger*/

#include<stdio.h>
#include<conio.h>

float abc(float);
int main(void)
{
    int sayi;
    printf("sayi gir:");
    scanf("%d",&sayi);
    printf("sayinin mutlak degeri:%f",abc(sayi));
    getch();
    
}

float abc(float x)
{    
     if(x<0)
         return -1*x;
     else
         return x;
         }    


