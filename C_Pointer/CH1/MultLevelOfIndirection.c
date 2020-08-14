
#include <stdio.h>

int main()
{
    
    char *titles[] = 
    {
       "A Tale of Two Cities", //0
       "Wuthering Heights",    //1
       "Don Quixote",          //2
       "Odyssey",              //3
       "Moby-Dick",            //4
       "Hamlet",               //5
       "Gulliver's Travels"    //6
    };  

    char **bestBooks[3];
    char **englishBooks[4];
    
    /////////////////////////////////////
    
    bestBooks[0] = &titles[0];
    bestBooks[1] = &titles[3];
    bestBooks[2] = &titles[5];
    
    englishBooks[0] = &titles[0];
    englishBooks[1] = &titles[1];
    englishBooks[2] = &titles[5];
    englishBooks[3] = &titles[6];
    
    printf("bestBooks[%d]=%s\n",0,*bestBooks[0]);         
    printf("bestBooks[%d]=%s\n",1,*bestBooks[1]);      
    printf("englishBooks[%d]=%s\n",1,*englishBooks[1]);

    return 0;
}
