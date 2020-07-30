#include <iostream>
#include <bits/stdc++.h>

using namespace std;
#define ll long long
const int maxN = 2e5;
int a[maxN];
int ans[maxN];
int n, x;

int main() {
    cin >> n >> x;
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    int ans = 0;
    int start = 0;
    int s = 0;
    for(int i = 0; i < n; i++){
        s += a[i];
        if(s == x){
            ans++;
        }else if(s > x){
            while(s > x && start <= i){
                s = s- a[start++];
                if (s == x){
                    ans++;
                }
            }
        }
    }
    
    cout << ans;
    return 0;
}
