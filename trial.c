#include <stdio.h>
#include <stdlib.h>

void helloWorld(const char *word){
   printf("%s\n",word);
}
int main(){
    helloWorld("printf");
    return 0;
}
