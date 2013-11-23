/*join ("abc", '-') -----> "a-b-c"*/

#include<stdio.h>
#include<conio.h>

int main(void)
{
    char kelime[10],yeni[15];
    int i,a;
    printf("kelime gir:");
    gets(kelime);
    for(i=0,a=0;kelime[i]!='\0';i++,a++)
    {
        yeni[a]=kelime[i];
        printf("%c",yeni[a]);
        a++;
        if(kelime[i+1]!='\0')
            yeni[a]='-';
            printf("%c",yeni[a]);
    }
    getch();
    return 0;
}
        
