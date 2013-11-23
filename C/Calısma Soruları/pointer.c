/*f pointerý için malloc yardýmýyla f pointerýnýn gösterdiði alana büyük bir sayý yerleþtirin . Daha sonra f pointerý i ve c pointerý ayný yeri göstersin . Ve daha sonra ekranda f nin i nin ve c nin gösterdiði deðer yazýlsýn 
i = (int * )f ;
c = (char*)f ;
f = (float*)f ;*/

#include<stdio.h>
#include<conio.h>

int main(void)
{
    float *f;
    int *i,z;
    char *c;
    f=(float*)malloc(sizeof(float));
    if(f==NULL)
    {
        printf("bellek dolu.");
        }
    for(z=0;z<10;z++)
        f[z]=z;
                
    printf("f nin adresi:%d\n",f);
    i=(int*)f;
    printf("i nin adresi %d\n",i);
    c=(char*)f;
    printf("c nin adresi: %d\n",c);
    for(z=0;z<10;z++)
        printf("%f\n",f[z]);
    free(f);
    getch();
    return 0;
}
