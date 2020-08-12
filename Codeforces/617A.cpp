#include <iostream>

using namespace std;

int main()
{
    int x, count=0;
    cin >> x;
    count = x/5;
    if (x%5 != 0) count++;
    cout << count;
	return 0;
}
