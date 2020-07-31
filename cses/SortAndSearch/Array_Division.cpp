#include <iostream>
#include <bits/stdc++.h>

using namespace std;
#define ll long long
const int maxN = 2e5;
ll a[maxN];
int n, k;

int main() {
    cin >> n >> k;
	ll s = 0, m = 1;
    for(int i = 0; i < n; i++){
        cin >> a[i];
		s += a[i];
		m = max(m, a[i]);
    }
	ll l = m, r = s;
    while (l < r){
		s = 0;
		m = (l+r) / 2;
		int c = 0;
		for(int i = 0; i < n; i++){
			if(s + a[i] > m){
				c++;
				s = 0;
			}
			s += a[i];
		}
        // cout << l << " " << r << " " << c << "\n";
		if(c >= k){
			l = m+1;
		}else{
			r = m;
		}
	}
    
    cout << l;
    return 0;
}
