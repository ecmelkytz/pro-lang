#include<stdio.h>
#include<conio.h>
#include<string.h>
int main(void)
{
    char yazi[50];
    int i;
    printf("yazi yaz:");
    gets(yazi);
    for(i=0;yazi[i]!='\0';i++)
    {
        if(isalpha(yazi[i]))
            printf("%c",yazi[i]);
        else if(isalpha(yazi[i-1]) && yazi[i]==' ')
            printf("%c",yazi[i]);
                       
    }
    getch();
    return 0;
}            
