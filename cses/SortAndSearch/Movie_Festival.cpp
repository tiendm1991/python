#include <iostream>
#include <bits/stdc++.h>
#include <set>
#define arr array<int, 2>

using namespace std;


int n, m;

int main()
{
    cin >> n;
    set<arr> s;
    int a, b;
    int ans = 0;
    for(int i = 0; i < n; i++){
        cin >> a >> b;
        s.insert({b, a});
    }
    int cur = -1;
    for(arr check: s){
        if(check[1] >= cur){
            ++ans;
            cur = check[0];
        }
    }

    cout<<ans;
}
