#include <iostream>
#include <bits/stdc++.h>

using namespace std;
#define ll long long
#define arr3 array<int, 3>
int n;
set<arr3 > s;

int main() {
    int count = 0;
    int maxRoom = 0;
    map<int, int> m;
    set<int> roomsAvailable;
    cin >> n;
    int ans[n];
    for (int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;
        s.insert({a, 1, -i});
        s.insert({b + 1, -1, -i});
    }
    for (auto x : s) {
        count += x[1];
        maxRoom = max(maxRoom, count);
        if (x[1] == -1) {
            roomsAvailable.insert(m.find(x[2])->second);
            m.erase(x[2]);
        }
        if (x[1] == 1) {
            if(roomsAvailable.empty()){
                roomsAvailable.insert(count);
            }
            int r = *roomsAvailable.begin();
            ans[-x[2]] = r;
            m.insert({x[2], r});
            roomsAvailable.erase(r);
        }
    }
    cout << maxRoom << "\n";
    for (int i = 0; i < n; i++) {
        cout << ans[i];
        if (i < n - 1) {
            cout << " ";
        }
    }

}
