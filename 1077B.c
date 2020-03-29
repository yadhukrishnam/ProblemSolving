/*
CodeForces Problem Code: 1077 B
Author: Yadhu Krishna M (AM.EN.U4CSE19264)
Written on: 29 March 2020
*/

#include <stdio.h>

int main() {
	int n, count=0;							
	scanf("%d", &n);
	int arr[n]; 

	for (int i=0; i<n; i++) 				// Inputs the array of N houses 
		scanf("%d", arr+i);					// Possible Inputs 0 or 1 indicating
											// lights in ON or OFF condition

	for (int i=0; i<n-2; i++) 				// Loops through the array
	{						
		if (arr[i] == 1 && arr[i+1]==0 && arr[i+2] == 1) 
		{
			arr[i+2] = 0;					// If the ith and i+2th house is ON, and 
			count++;						// i+1 the house (ie. house in middle) is OFF
											// Value of count should be incremented.
											// and the i+2th house is turned off.
		}
	}
	printf("%d", count);					// Outputs count and exits.
	return 0;
}
