/*13 ve 17'ye bölünüp bölünememe hesabı*/

#include<stdio.h>
#include<conio.h>
int main(void)
{
    int sayi;
    printf("sayi gir:");
    scanf("%d",&sayi);
    if((sayi%13==0) && (sayi%17!=0))
        printf("13'e bolunuyor.");
    else if((sayi%13!=0) && (sayi%17==0))
        printf("17'ye bolunuyor.");
    else if((sayi%13==0) && (sayi%17==0))
        printf("13 ve 17'ye bolunuyor.");
    else if((sayi%17!=0) && (sayi%13!=0))
        printf("13 ve 17'ye bolunmuyor.");
    
    getch();
    return 0;
}                
    
