#include<stdio.h>
int fonksiyon(float x)
{
    float fonk=x*x*x+4*x*x-10;
    print ("%f",fonk);
}
int main(void)
{
    int a,b;
    float yarim;
    int d=1,son;
    printf("sinir araliklarini giriniz:");
    scanf("%d %d",&a,&b);

    while (d)
    {
          if fonksiyon(a)*fonksiyon(b)>0
          {
              printf("%f ve %f arasinda fonksiyonun koku yoktur.",a,b);
              yarim=(a+b)/2;
              a=yarim;
              }
          else if fonksiyon(a)*fonksiyon(b)==0
          {
               if fonksiyon(a)==0 and fonksiyon(b)==0
               {
                   printf ("%f ve %f fonksiyonun kokleridir.",a,b);
                   }
               else if fonksiyon(a)==0
               {
                    printf ("%f fonksiyonun kokudur.",a);
                    }
                    else if fonksiyon(b)==0
                    {
                         printf ("%f fonksiyonun kokudur.",b);
                         }
                         
         else if fonksiyon(a)*fonksiyon(b)<0
         {
              printf ("%f ve %f arasýnda bir kok vardir.",a,b);
              yarim=(a+b)/2;
              b=yarim;
              }
        printf("devam etmek istiyorsan 1 yaz istemiyorsan 0 yaz:");
        scanf("%d",&son);
        if son==0
        {
            d=0;
            }
         else
         {
             d=1;
             }              
    }
    getch();
    return 0;
}    
              
              
                                
                   

          
          
          
    
