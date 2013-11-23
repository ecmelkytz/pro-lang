/* Virgülden sonra kaç basamak yuvarlamak istiyorsak o kadar yuvarlayan fonksiyon*/

#include<stdio.h>
#include<conio.h>
#include<math.h>

int yuvarla(float ,int);
int main(void)
{
    float sayi,islem;
    int bas;
    printf("sayi gir\n");
    scanf("%f",&sayi);
    printf("virgulden sonra yuvarlanmasini istediginiz basamak sayisi:\n");
    scanf("%d",&bas);
    yuvarla(sayi,bas);
    getch();
    return 0;
    
}
int yuvarla(float sayi,int basamak)
{
    switch(basamak)
    {
        case 1: printf("sayinin yuvarlanmis hali:%4.1f",sayi);break;
        case 2: printf("sayinin yuvarlanmis hali:%4.2f",sayi);break;
        case 3: printf("sayinin yuvarlanmis hali:%4.3f",sayi);break;
        case 4: printf("sayinin yuvarlanmis hali:%4.4f",sayi);break;
        case 5: printf("sayinin yuvarlanmis hali:%4.5f",sayi);break;
        default: printf("sayinin yuvarlanmis hali:%4.6f",sayi);break;
    }
}
