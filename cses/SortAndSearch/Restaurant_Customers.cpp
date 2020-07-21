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
        s.insert({a,1});
        s.insert({b,-1});
    }
    int cur = -1;
    int c = 0;
    for(arr x : s){
        c += x[1];
        ans = max(ans, c);
    }
    
    cout<<ans;
}
