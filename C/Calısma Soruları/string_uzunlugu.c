/*null degerine kadar sayan ve stringin uzunlugunu veren fonksiyon*/

#include<stdio.h>
#include<conio.h>

int main(void)
{
    char str[50];
    int i,say=0;
    gets(str);
    for(i=0;str[i]!='\0';i++)
    {
        say++;
        }
    printf("string %d uzunlugunda.",say);
    getch();
    return 0;
}    
