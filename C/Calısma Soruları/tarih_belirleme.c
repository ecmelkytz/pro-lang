/*Ay ve gün verildiginde yilin kacinci günü oldugunu bulan kod*/

#include<conio.h>
#include<stdio.h>
#define YIL 365
int main(void)
{
    int ay,gun;
    printf("Bulundugunuz gun ve ayini giriniz sayi olarak:");
    scanf("%d%d",&gun,&ay);
    switch(ay)
    {
        case 1: gun=gun; break;
        case 2: gun=31+gun; break;
        case 3: gun=28+31+gun; break;
        case 4: gun=28+31+30+gun; break;
        case 5: gun=28+31+30+31+gun; break;
        case 6: gun=28+31+30+31+30+gun; break;
        case 7: gun=28+31+30+31+30+31+gun; break;
        case 8: gun=28+31+30+31+30+31+30+gun; break;
        case 9: gun=28+31+30+3130+31+30+31+gun; break;
        case 10: gun=28+31+30+31+30+31+30+31+30+gun; break;
        case 11: gun=28+31+30+31+30+31+30+31+30+31+gun; break;
        case 12: gun=28+31+30+31+30+31+30+31+30+31+30+gun; break;
        }
     printf("yilin %d gunundesiniz.",gun);
     getch();
     return 0;
            }
