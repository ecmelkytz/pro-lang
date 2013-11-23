/*Kelimenin bas harflerinin alarak kisaltma. Avrupa Birliği = AB  gibi*/

#include<stdio.h>
#include<conio.h>
int fonk(char cumle[],char kelime[])
{
    int i,a=1;
    kelime[0]=cumle[0];
    for(i=1;cumle[i]!='\0';i++)
        if(cumle[i]==' ')
        {  
            kelime[a]=cumle[i+1];
            a++;
        }
    
}
int main(void)
{
    char c[100],k[30];
    int i;
    printf("Bir dizgi giriniz:");
    gets(c);
    while(c[0]!='\0')
    {
        fonk(c,k);
        printf("kisaltma:%s\n\n",k);
        printf("bir dizgi gir:");
        gets(c);
    }
    getch();
    return 0;
}           
    
