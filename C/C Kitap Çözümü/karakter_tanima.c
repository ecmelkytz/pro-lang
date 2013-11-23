/*girilen degerin harf mi özel karakter mi yoksa sayı mı oldugunu bulma*/

#include<stdio.h>
#include<conio.h>


int fonk(char x)
{
    if('0'<=x && x<='9')
       return(1);
    else if('A'<=x && 'Z'>=x || 'a'<=x && 'z'>=x)
       return(2);
    else return(3);
}
int main(void)
{
    char ch;
    int sonuc,i,enter;
    printf("Pozitif  bir tamsayi gir:");
    scanf("%d",&i);

    while(i>0)
    {
              printf("karakter giriniz:");
              scanf(" %c",&ch);
    
              sonuc=fonk(ch);
              i-=1;
              switch(sonuc)
              {
                  case 1: printf("%c sayi karakterdir.\n",ch);
                          break;
                  case 2: printf("%c alfabetik karakteridir.\n",ch);
                          break;   
                  case 3: printf("%c ozel karakterdir.\n",ch);
              }
    }
    getch();
    return (0);
}
                  
    
