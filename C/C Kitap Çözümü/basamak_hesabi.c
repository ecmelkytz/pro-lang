/*sayının basamak sayısını hesaplama*/

#include<stdio.h>
#include<conio.h>

int basamak(int);
int main(void)
{
    int sayi;
    printf("pozitif sayi giriniz:");
    scanf("%d",&sayi);
    while(sayi>0)
    {
        printf("basamak degeri:%d\n",basamak(sayi));
        printf("pozitif sayi gir:");
        scanf("%d",&sayi);
    }
       
    getch();
    return 0;
}
int basamak(int x)
{
    int islem,say;
    for(say=1;x>9;say++)
    {
        x=x/10;
    }
    return say;
}
