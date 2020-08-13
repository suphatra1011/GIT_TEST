#include <stdio.h>

#define FORMAT(x) \
    _Generic((x), \
        int: "int", \
        char: "char", \
        long: "long", \
        float: "float", \
        long long: "long long" )

char ary[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
char *p1 = ary;
char *p2;
int *pn;

void test()
{   //p1[0] = 0
    printf("\r\nchar-p1=%p,*p1=0x%x",p1,*p1); //p1=0x556158346010
    p1+=2;                  //p1[0] = 2     
    printf("\r\nchar2-p1=%p,*p1=0x%x",p1,*p1); //p1=0x556158346012
    
    printf("\r\n1-pn=%p",pn); //
    pn = (int*)&p1[2];     //p1[2] = 4, char->int之後，pn[0] = 7
    printf("\r\n(int*)&p1[2]=%p",(int*)&p1[2]);//0x556158346014
    
    printf("\r\nint-pn=%p,*pn=0x%x",pn,*pn); //pn=0x5621cb222014
    
    pn+=1;                  //加完之後pn[0] = 8  (因為是int型態)
    printf("\r\nint2-pn=%p, *pn=0x%x",pn,*pn); //pn=0x5621cb22201c
    //Q
    
    ////////////////////
    p1 = (char*)pn;        //pn從int->char，維持在原位，p1[0]=8
    printf("\r\nchar-pn=%p",pn); //pn=0x5621cb22201c
    printf("\r\nchar-p1=%p,*p1=0x%x",p1,*p1); //p1=0x5621cb22201c
    --pn;                   
    printf("\r\nchar-pn=%p",pn); //pn=0x5621cb222018
    //因為pn是int型別，做加減法會位移4個byte而不是1個byte，所以pn[0]=4
    
    p2 = (char*)pn;        //int->char不會縮減，所以p2[0]=4
    printf("\r\nchar-pn=%p",pn); //pn=0x5621cb222018
    printf("\r\nchar-p2=%p",p2); //p2=0x5621cb222018
    --p2;                   
    printf("\r\nchar-p2=%p,*p2=0x%x",p2,*p2); //p2=0x5621cb222017
    //p2是char，所以只會減1個byte，p2[0]=3
}

int main()
{
    test();
    printf("\r\n*p1 = 0x%x *p2= 0x%x\n", *p1, *p2);
    return 0;
}
