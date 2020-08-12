#include <stdio.h>

int main () {
    int len, n=0, z=0 ;
    scanf("%d", &len);
    char s[len];
    scanf("%s", s);
    for (int i=0; i<len; i++)
        if (s[i] == 'n')
            n++;
        else if (s[i] == 'z')
            z++;

    while(n--) printf("1 ");
    while(z--) printf("0 ");
    
}
