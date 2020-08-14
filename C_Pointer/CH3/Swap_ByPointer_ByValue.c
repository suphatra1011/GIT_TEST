#include <stdio.h>
void swapByPointer(int *ptrNum1,int *ptrNum2) //CallByAddress
{
    int Temp=0;
    Temp = *ptrNum1;
    *ptrNum1 = *ptrNum2;
    *ptrNum2 = Temp;
}

void swapByValue(int Num1,int Num2)          //CallByValue
{
    int Temp=0;
    Temp = Num1;
    Num1 = Num2;
    Num2 = Temp;
    
    printf("\r\nInVal-Num1=%d at %p, Num2=%d at %p",Num1,&Num1,Num2,&Num2);
}

int main() 
{
    int Num1=5,Num2=10;
    swapByValue(Num1,Num2);
    printf("\r\nOutVal-Num1=%d at %p, Num2=%d at %p",Num1,&Num1,Num2,&Num2);
    
    Num1=5,Num2=10;
    swapByPointer(&Num1,&Num2);
    printf("\r\nPointer-Num1=%d at %p, Num2=%d at %p",Num1,&Num1,Num2,&Num2);
    
    return 0;
}
