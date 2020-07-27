#include <iostream>
#include <bits/stdc++.h>

using namespace std;
#define ll long long
#define arr array<int, 2>
const int maxX = 1e9, maxN = 2e5;
int x, n;
set<int> s;
set<arr > a;

int main() {
    s.insert(0);
    cin >> x >> n;
    s.insert(x);
    a.insert({-x, 0});
    for (int i = 0; i < n; i++) {
        int p;
        cin >> p;
        auto search = s.lower_bound(p);
        int end = *search;
        --search;
        int start = *search;
        s.insert(p);
        a.erase({start - end, start});
        a.insert({start - p, start});
        a.insert({p - end, p});
        auto ans = a.begin();
        cout << -((*ans)[0]);
        if (i < n - 1) {
            cout << " ";
        }
    }


}
