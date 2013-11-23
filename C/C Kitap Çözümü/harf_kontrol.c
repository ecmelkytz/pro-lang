/*Herhangi bir karakteri alan ve bu karakterin harf olup olmadığını döndüren program*/

#include<stdio.h>
#include<conio.h>

int main(void)
{
    char x;
    printf("Bir karakter giriniz:");
    scanf("%c",&x);
    if(isalpha(x))
    {    
        if('A'<x && 'Z'>x)
            printf("%c bir buyuk harftir.",x);
        else if('a'<x && 'z'>x)
            printf("%c bir kucuk harftir.",x);
    }
    else
    printf("%c bir harf degildir.",x);
    getch();
    return 0;
}    
