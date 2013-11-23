/*String içerisindeki \n ile baþlayan özel karakterleri bulan program
Ayrica \n olan yerleri * ile degistirir */

#include<stdio.h>
#include<conio.h>
int main(void)
{
    char cumle[50];
    int i;
    printf("cumle gir:");
    gets(cumle);
    for(i=0;cumle[i]!='\0';i++)
    {
        if(isspace(cumle[i]))
        {
            putchar('*');
            }   
        else
            putchar(cumle[i]);
    }
    getch();
    return 0;
    }           
