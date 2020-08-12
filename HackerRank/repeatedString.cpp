#include <bits/stdc++.h>

using namespace std;

long repeatedString(string s, long n) {
    long l = s.length();
    long count = 0, rem = n%l;
    long i = 0;
    for (; s[i]!='\0';)
        count += s[i++] == 'a';
    count *= n/l;
    for (i=0; i<rem;)
        count += s[i++] == 'a';
    return count;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    long n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    long result = repeatedString(s, n);

    fout << result << "\n";

    fout.close();

    return 0;
}
