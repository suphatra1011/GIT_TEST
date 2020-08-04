#include <stdio.h>

//Case-1
//#define MAXSIZE 10

//Case-2 To suggest the method to replace Case-1 pre-define
const unsigned char MAXSIZE=10;

int main()
{
    static unsigned char* arrRspData=NULL;
    
#if 1
    //Case-1 
    arrRspData = (unsigned char*)malloc( MAXSIZE * sizeof(unsigned char));
    memset(arrRspData,5,MAXSIZE * sizeof(unsigned char));
#else
    //Case-2
    arrRspData = (unsigned char*)calloc( MAXSIZE, sizeof(unsigned char)); // memory allocation and init value 0
#endif    

    for(int Cnt=0;Cnt<MAXSIZE;Cnt++)
    {
        printf("arrRspData[%d]=%x\r\n",Cnt,arrRspData[Cnt]);
    }
    
    free(arrRspData); //To release memory
    
    return 0;
}
