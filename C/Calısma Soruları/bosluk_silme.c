/*Cümlenin önündeki ve sonundaki fazla bosluklari siler*/

#include<conio.h>
#include<stdio.h>
#include<string.h>
int main(void)
{
    char cumle[50];
    int i;
    printf("Cumle gir:");
    gets(cumle);
    
    for(i=0;cumle[i]!='\0';i++)
    {
        if(cumle[i]==' ' && cumle[i-1]==' ')
        {
            i++;
            }
        else    
            putchar(cumle[i]);
    }
    getch();
    return 0;
}    
