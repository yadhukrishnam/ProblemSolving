#include <stdio.h>

int main(){
	int n, j =0,x,flag;
	scanf("%d", &n);
	int arr[n];
	while (n--){
		scanf("%d", &x);
		if (x) {
			flag = 1;
			for(int i=0; i<j; ) {
				if (arr[i++] == x) {
					flag = 0;
					break;
				} 
			}
			if (flag) arr[j++] = x;
		}
	}
	printf("%d", j);
}
