#include <iostream>
#include <bits/stdc++.h>
 
using namespace std;
#define ll long long
const int maxN = 1e5;
const ll maxV = 1e15;
ll a[maxN + 1];
vector<ll> ans[maxN + 1];
vector<array<ll, 2>> adj[maxN + 1];
int n, m, k;
 
 
int main() {
 
    cin >> n >> m >> k;
    for (int i = 1; i <= m; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        adj[a].push_back({b, c});
    }
    //min heap
    priority_queue<array<ll, 2>, vector<array<ll, 2>>, greater<array<ll, 2>>> pq;
    pq.push({0, 1});
    while (!pq.empty()) {
        array<ll, 2> cur = pq.top();
        pq.pop();
		if(ans[cur[1]].size() >= k){
			continue;
		}
		ans[cur[1]].push_back(cur[0]);
        for (array<ll, 2> x: adj[cur[1]]) {
			pq.push({cur[0] + x[1], x[0]});
        }
    }
	for (int i = 0; i < k; i++){
		cout << ans[n][i] << " ";
	}
    return 0;
}
