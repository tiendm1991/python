#include <iostream>
#include <bits/stdc++.h>

using namespace std;
#define ll long long
const int maxN = 1e3;
int a[maxN];
int n, x;

int main() {
    cin >> n >> x;
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    if(x < 4){
        cout << "IMPOSSIBLE";
        return 0;
    }
    unordered_map<int, array<int, 2>> mp;
    mp.reserve(1<<20);
    for(int i = 0; i < n-1; i++){
        for(int j = i+1; j < n; j++){
            int ij = a[i] + a[j];
            if(mp.find(x - ij) != mp.end()){
                array<int, 2> p = mp[x - ij];
                if(p[0] != i && p[1] != j && p[0] != j && p[1] != i){
                    cout << i+1 << " " << j+1 << " " << p[0] + 1 << " " << p[1]+1;
                    return 0;
                }
            }
            mp[ij] = {i, j};
        }
    }
    cout << "IMPOSSIBLE";
    return 0;
}
