/*String palindrom ise 1  degilse 0*/

#include<stdio.h>
#include<conio.h>
#include<string.h>

int main(void)
{
    char kelime[10],yeni[10];
    int i,u,a;
    gets(kelime);
    u=strlen(kelime)-1;
    for(i=u,a=0;i>=0;i--,a++)
    {
        yeni[a]=kelime[i];
    }
    if(strcmp(kelime,yeni)==0)
        printf("1");
    else
        printf("0");
    getch();
    return 0;
} 
        
