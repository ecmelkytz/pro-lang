/*bosluk silme*/

#include<stdio.h>
#include<conio.h>

int main(void)
{
    char dizgi[100];
    int i;
    printf("bir dizgi giriniz:\n");
    gets(dizgi);
    for(i=0;i<strlen(dizgi);i++)
    {
        if(dizgi[i]==' ' && dizgi[i+1]==' ' && dizgi[i+2]!=' ')
        {
            i++;
            printf("%c",dizgi[i]);
        }
        else if(dizgi[i]==' ' && dizgi[i+1]==' ')
        {
             i++;
        }
        printf("%c",dizgi[i]);
    }
    getch();
    return 0;
}    
