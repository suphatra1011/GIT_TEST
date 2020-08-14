
#include <stdio.h>
int main(int argc, char* argv[])
{
    char *a; 
    short *b; 
    int *c; 
    long int *d; 
    float *e; 
    double *f;
    printf("sizeof char: %lu\n", sizeof(*a));
    printf("sizeof short: %lu\n", sizeof(*b));
    printf("sizeof int: %lu\n", sizeof(*c));
    printf("sizeof long int: %lu\n", sizeof(*d));
    printf("sizeof float: %lu\n", sizeof(*e));
    printf("sizeof double: %lu\n", sizeof(*f));

    return 0;
}
