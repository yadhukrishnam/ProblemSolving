#include <stdio.h>

int main(){
	int a,b,candles;
	scanf("%d %d", &a, &b);
	candles = a;
	while (a/b > 0){
		candles+=a/b;
		a=a%b+a/b;
	}
	printf("%d", candles);
	return 0;
}
