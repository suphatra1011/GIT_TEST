#include <stdio.h>

int main(void) 
{
    int *A = 0;
    printf("A Address：%p\n", A);
    printf("A + 1：%p\n", A + 1);
    printf("A + 2：%p\n", A + 2);
    
    double *B = 0;
    printf("B Address：%p\n", B);
    printf("B + 1：%p\n", B + 1);
    printf("B + 2：%p\n", B + 2);

    int *C = (int *)0x2010;  
    
    printf("%x\n",C-2);               //2008  
    printf("%x\n",(float *) C-2);     //2008
    printf("%x\n",(double **)C-2);    //2008 
    printf("%x\n",(long long *)C-2);  //2000
    printf("%x\n",(short *)C-2);      //200c 
    printf("%x\n",(char *)C-2);       //200e  
    printf("%x\n",(unsigned long)C-2);//200e

    return 0;
}
