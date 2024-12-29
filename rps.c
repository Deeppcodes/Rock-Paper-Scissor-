#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>

int play(char human, char pc) {
    //s stone, p paper, c scissor
    if (human==pc)
        return -1;
    else if (human=='s' && pc=='p')
        return 2;
    else if (human=='p' && pc=='s')
        return 1;
    else if (human=='c' && pc=='s')
        return 2;
    else if (human=='s' && pc=='c')
        return 1;
    else if (human=='c' && pc=='p')
        return 2;
    else if (human=='p' && pc=='c')
        return 1;
}
int main(){
    int n;
    int lower=1,upper=3;
    char human, pc, result;
    srand(time(NULL));
    n=(rand()% (upper-lower+1))+lower;
    if (n=1){
        pc='s';
    }
    else if (n=2){
        pc='p';
    }
    else{
        pc='c';
    }
    
    printf("enter s/p/c:");
    scanf("%s",&human);
    
    result=play(human, pc);
    if (result==-1) {
        printf("it's a draw\n");
    }
    else if (result==1){
        printf("you won! :)\n");
    }
    else {
        printf("you lost! :(\n");
    }
    
    printf("you chose %c computer chose %c\n", human, pc);
    
    return 0;
    
}