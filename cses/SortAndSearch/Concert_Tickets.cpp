#include <iostream>
#include <bits/stdc++.h>
#include <set>

#define arr array<int, 2>

using namespace std;

const int maxN = 2e5, maxM = 2e5;
int n, m;
set<arr > h;

int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        h.insert({x, i});
    }
    for (int i = 0; i < m; i++) {
        int c;
        cin >> c;
        auto search = h.upper_bound({c + 1, 0});
        if (search == h.begin()) {
            cout << "-1\n";
        } else {
            --search;
            cout << (*search)[0] << "\n";
            h.erase(search);
        }
    }
}
