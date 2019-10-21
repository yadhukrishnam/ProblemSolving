#include <iostream>

using namespace std;

int main()
{
    int n, j,count=0;
    cin >> n;
    for(int i=0;i<n;i++){
        cin >>j;
        if (j==1)
            count++;
    }
    if (count>0)
        cout << "HARD";
    else
        cout << "EASY";


	return 0;
}
