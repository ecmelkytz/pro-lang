/*Stringi tersten yazdirma*/

#include<stdio.h>
#include<conio.h>
#include<string.h>

int main(void)
{
    char kelime[20];
    int i;
    printf("yazi yaz:");
    scanf("%s",&kelime);
    for(i=strlen(kelime)-1;i>-1;i--)
    {
        putchar(kelime[i]);
        }
    getch();
    return 0;
}
