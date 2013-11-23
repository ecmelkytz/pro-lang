/*"ahmet 29 ayse 88 duygu 55" gibi bir dizgiyi 
ahmet 29
ayse 88 
seklinde satir satir bolme */

#include<stdio.h>
#include<conio.h>

int main(void)
{
    char dizgi[100];
    int i;
    printf("isim ve notlari gir:");
    gets(dizgi);
    printf("liste:\n");
    for(i=0;i<strlen(dizgi);i++)
    {                        
        if(dizgi[i]>='0' && dizgi[i]<='9' && dizgi[i+1]==' ')
        {
            printf("%c",dizgi[i]);             
            printf("\n");
            i++;
        }
        else
        printf("%c",dizgi[i]);
    }    
    getch();
    return 0;
}
