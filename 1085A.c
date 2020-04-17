#include <stdio.h>
#include <string.h>

int main() {
    int n,start;
    char str[60];
    scanf("%s",str);
    n = strlen(str);
    n = n%2?n/2:n/2-1;
    printf("%c", str[n]);
    for(int i=1; i <= n; i++) 
    printf("%c%c",str[n+i],str[n-i]);
    if (n%2 == 0)printf("%c", str[strlen(str)-1]);
}