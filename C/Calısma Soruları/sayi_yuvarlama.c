/*sayi yuvarlama*/

#include<stdio.h>
#include<conio.h>

int yuvarla(float);
int main(void)
{
    float sayi;
    printf("sayi gir:");
    scanf("%f",&sayi);
    printf("sayinin tamsayiya yuvarlanmis hali:%d",yuvarla(sayi));
    getch();
    return 0;
}
int yuvarla(float x)
{
    int i;
    float k;
    i=(int)x;
    k=x-(float)i;
    if(k<=0.5)
        return i;
    else
       return i+1;
       }    
