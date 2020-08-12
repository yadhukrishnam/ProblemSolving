#include <stdio.h>
#include <string.h>

int main () {
    int n, flag, i, j;
    scanf("%d", &n);
    char names[n][120];

    for(i=0; i<n; i++)
    {
        flag = 0;
        scanf("%s", names[i]);
        for (j=0; j<i; j++)
            if (strcmp(names[i], names[j]) == 0) {
                flag = 1;
                break;
            }
        if (flag == 1)
            printf("YES\n");
        else 
            printf("NO\n");
    }
}
