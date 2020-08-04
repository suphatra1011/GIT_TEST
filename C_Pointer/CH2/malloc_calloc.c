#include <stdio.h>

//[TIPS-1]Suggest to use const to preprocessor.
//Difference and advantages can refer https://www.jianshu.com/p/4d9f30abc3e9
#if 1
    //Case-1:Pre
    #define MAXSIZE 10
#else
    //Case-2: Run-Time 
    const unsigned char MAXSIZE=10;
#endif

//void free_mem(unsigned char* ptr)
void free_mem(void *ptr)
{
    if(ptr != NULL)
    {
        free(ptr);
        ptr=NULL;
    }
}

/*------- Main -------*/
int main()
{
    static unsigned char* arrRspData=NULL;
    
//[TIPS-2]Usage: malloc/calloc
#if 1
    //Case-1 
    arrRspData = (unsigned char*)malloc( MAXSIZE * sizeof(unsigned char));
    memset(arrRspData,5,MAXSIZE * sizeof(unsigned char));
#else
    //Case-2
    arrRspData = (unsigned char*)calloc( MAXSIZE, sizeof(unsigned char)); // memory allocation and init value 0
#endif    

//[TIPS-3]Confirm memory allocate sucessfully, to avoid memory leak or crash.
    if( (arrRspData != NULL) && MAXSIZE !=0) 
    {
        for(int Cnt=0;Cnt<MAXSIZE;Cnt++)
        {
            printf("arrRspData[%d]=%x\r\n",Cnt,arrRspData[Cnt]);
        }
        
//[TIPS-4]
    #if 1
        free(arrRspData); //To release memory
        arrRspData=NULL;  
    #else
        free_mem(arrRspData);
    #endif
        
        if(arrRspData!=NULL)
        {
            printf("Fail to free memory.\r\n");
        }
    }
    return 0;
}
