#include <iostream>
#include <bits/stdc++.h>

using namespace std;
#define ll long long
const int maxN = 2e5;
int a[maxN];
int ans[maxN];
int n;

int main() {
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    stack<int> s; 
    s.push(0);
    for(int i = 1; i < n; i++){
        while(!s.empty() && a[s.top()] >= a[i]){
            s.pop();
        }
        if(!s.empty()){
            ans[i] = s.top() + 1;
        }
        s.push(i);
    }
    cout << ans[0];
    for(int i = 1; i < n; i++){
        cout << " " << ans[i];
    }
    return 0;
}
