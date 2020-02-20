#include <stdio.h>
int main(){
	int t,p,q, count=0;
	scanf("%d", &t);
	while (t--){
		scanf("%d %d", &p, &q);
		if (q-p >= 2)
			count++;
	}
	printf("%d", count);
}
