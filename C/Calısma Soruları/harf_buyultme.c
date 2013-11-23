/*Küçük harfleri büyültme*/

#include<stdio.h>
#include<conio.h>

int main(void)
{
    char yazi[50];
    int i;
    gets(yazi);
    for(i=0;yazi[i]!='\0';i++)
    {
        if(islower(yazi[i]))
        {
            yazi[i]=toupper(yazi[i]);
            putchar(yazi[i]);
            }
        else if(isupper(yazi[i]))
        {
            yazi[i]=tolower(yazi[i]);
            putchar(yazi[i]);
            }
        else
            putchar(yazi[i]);    
    }
    getch();
    return 0;
}    
            
