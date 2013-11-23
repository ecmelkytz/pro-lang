/*Kelimenin içinde nano yazıyorsa true yazmıyorsa false*/

#include<stdio.h>
#include<conio.h>

int main(void)
{
    char yazi[50],ic[10];
    printf("yazi yaz:");
    gets(yazi);
    printf("yazinin icinde aradigin kelimeyi yaz:");
    gets(ic);
    if(strstr(yazi,ic))
        printf("True");
    else
        printf("False");
    getch();
    return 0;
}        
