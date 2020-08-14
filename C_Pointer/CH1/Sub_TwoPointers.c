
#include <stdio.h>

int main()  
{  
    int arr[10] = {0};//x  
    int *p = &arr[9]; //x+36  
    int *q = &arr[1]; //x+4  
    
    printf("%d\n",p-q);                      //8  
    printf("%d\n",q-p);                      //-8  
    printf("%d\n",(short *)p-(short *)q);    //16  
    printf("%d\n",(long *)p-(long *)q);      //8  
    printf("%d\n",(char **)p-(char **)q);    //8  
    printf("%d\n",(double *)p-(double *)q);  //4  
    printf("%d\n",(long long)p-(long long)q);//32  
    printf("%d\n",(char *)p-(char *)q);      //32  
  
    return 0;  
}    
