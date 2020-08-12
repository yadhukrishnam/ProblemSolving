#include <stdio.h>

int main(){
    char hello[5] = {'h','e','l','l','o'};
    char s[100], prev;
    
    int cur = 0, score=0;
    scanf("%s", s);
    for (int i=0; s[i]!='\0'; i++){
        if (s[i] == hello[cur]) {
            cur++;
            score++;
        }
        if (score == 5)
            break;
    }
    if (score == 5)
        printf("YES");
    else 
        printf("NO");
    
}
