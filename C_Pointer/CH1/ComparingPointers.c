#include <stdio.h>

void main (void) 
{
        int var[]={11, 22, 33, 44};
        int i=0, *ptr;

        ptr=var;
        while ( ptr <= &var[sizeof(var)/sizeof(int)-1]) 
        {
          printf( "var[%d]=%d\t&var[%d]=%x\n", i, var[i], i, &var[i]);
          printf( "*ptr=%d\t\tptr=%x\n", *ptr, ptr);
          ptr++;
          i++;
        }
}
