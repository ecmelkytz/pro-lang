/*cumle icinde en kisa kelimeyi bulma*/

#include<stdio.h>
#include<conio.h>

int main(void)
{
    char cumle[100];
    int uzunluk[20];
    int say=0,i,a=0,min,sira=1,u,son=0;
    gets(cumle);
    for(i=0;cumle[i]!='\0';i++)
    {
        if(cumle[i]!=' ')
        {
            uzunluk[a]=say;
            say++;
        }
        u=say-1;
    }
    min=uzunluk[0];
    for(i=1;i<u;i++)
    {
        if(min>uzunluk[i])
        {
            min=uzunluk[i];
            sira++;
        }
    }
    
    for(i=0;i<strlen(cumle);i++)
    {
        if(son!=sira)
        {
            if(cumle[i]==' ')
            {
                son++;
            }
        }
        else
        if(cumle[i]!=' ')
            printf("%c",cumle[i]);
    }               
    getch();
    return 0;
}
/*
int main(void)
{
    char c[100],k[30];
    printf("bir cumle giriniz:");
    gets(c);
    kisa(c,k);
    printf("en kisa cumle:%s",k);
    getch();
    return 0;
}
*

