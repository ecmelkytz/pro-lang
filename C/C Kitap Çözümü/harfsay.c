/*Harf hesabi*/

#include<stdio.h>
#include<conio.h>

int main()
{
    int say=0,i;
    char yazi[20];
    printf("yazi yaz:");
    gets(yazi);
    for(i=0;yazi[i]!='\0';i++)
        if(yazi[i]=='m')
            say+=1;
        
    printf("yazida %d tane m harfi var",say);
    getch();
    return(0);
}    
            
