#include <iostream>
#include <bits/stdc++.h>

using namespace std;
#define ll long long
const int maxN = 5e3;
int a[maxN];
int n, x;

int main() {
    cin >> n >> x;
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    if(x < 3){
        cout << "IMPOSSIBLE";
        return 0;
    }
    unordered_map<int, int> mp;
    mp.reserve(1<<20);
    for(int i = 0; i < n-1; i++){
        for(int j = i+1; j < n; j++){
            int ij = a[i] + a[j];
            if(mp.find(x - ij) != mp.end()){
                int k = mp[x - ij];
                if(i != k && j != k){
                    cout << i+1 << " " << j+1 << " " << k + 1;
                    return 0;
                }
            }
        }
        mp[a[i]] = i;
    }

    cout << "IMPOSSIBLE";
    return 0;
}
