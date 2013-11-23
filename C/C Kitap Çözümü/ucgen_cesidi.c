/*ucgen çeşidini hesaplama*/

#include<stdio.h>
#include<conio.h>

int main(void)
{
    int a,b,c,toplam,islem;
    printf("uc aci gir:");
    scanf("%d %d %d",&a,&b,&c);
    toplam=a+b+c;
    if(toplam==180)
        if(a==90 || b==90 || c==90)
            printf("bu bir dik acili ucgen");
        else if(a>90 || b>90 || c>90)
            printf("bu bir genis acili ucgen");
        else if(a<90 && b<90 && c<90)
            printf("bu bir dar acili ucgen");
    else
    printf("ucgen degil");
    getch();
    return 0;
}                
