/*matrisin minor ve major köşegen elemanlarını 1 diğer elemanlarını 0 yap*/

#include<stdio.h>
#include<conio.h>

int main(void)
{
    char dizi[10][10];
    int a,b,n;
    printf("matrisin boyutunu gir:");
    scanf("%d",&n);
    for(a=0;a<n;a++)
        for(b=0;b<n;b++)
            dizi[a][b]=0; 
        
    
   for(a=0;a<n;a++)
   {
       dizi[a][a]=1;
       dizi[a][n-a-1]=1;
   }
   
   for(a=0;a<n;a++)    
   {
       for(b=0;b<n;b++)
           printf("%d",dizi[a][b]);
       printf("\n");    
   }
      
   getch();
   return 0;
}              
