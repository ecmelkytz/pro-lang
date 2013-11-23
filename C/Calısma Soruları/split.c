/*split ("a-b-c", '-') -----> " abc"*/

#include<stdio.h>
#include<conio.h>

int main(void)
{
    char kelime[10],yeni[5];
    int i,a;
    gets(kelime);
    for(i=0,a=0;kelime[i]!='\0';i++,a++)
    {
        if(kelime[i]!='-')
        {
            yeni[a]=kelime[i];
            printf("%c",yeni[a]);
            }
        else
            a--;    
    }     
    getch();      
    return 0;
}        
            
