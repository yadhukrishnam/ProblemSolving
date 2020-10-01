#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        priority_queue<int> soldiers;
        int N, Z, temp;
        cin >> N >> Z;
        for (int i = 0; i < N; i++)
        {
            cin >> temp;
            soldiers.push(temp);
        }

        int ctr = 0;
        while (soldiers.top()!=0 && Z>0)
        {
            int max = soldiers.top();
            Z -= max;
            soldiers.pop();
            soldiers.push(max / 2);
            ctr++;
        }

        if (Z > 0)
            cout << "Evacuate" << endl;
        else
            cout << ctr << endl;
    }
}
