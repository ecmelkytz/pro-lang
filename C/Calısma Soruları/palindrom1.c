/*palindrom olup olmadigini bulma*/

#include<stdio.h>
#include<conio.h>
#include<string.h>
int main(void)
{
    char x[10];
    int a,b,durum=1;
    
    printf("kelime yaz:");
    scanf("%s",&x);
    for(a=0,b=strlen(x)-1;a<=(strlen(x)/2);a++,b--)
    {
         if(x[a]==x[b])
         {
             durum*=1;
             }
         else
         {
             durum*=0;
             }
    }
    if(durum==1)
        printf("palindromdur: %d",durum);
    else
        printf("palindrom degildir: %d",durum);
    getch();
    return 0;
}                   
    
