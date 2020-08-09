#include <iostream>
#include <bits/stdc++.h>
 
using namespace std;
#define ll long long
const int maxN = 1e5;
const ll maxV = 1e15;
ll d[maxN + 1], d_back[maxN + 1];
vector<array<ll, 2>> adj[maxN + 1], adj_back[maxN + 1];
int n, m;
 
int dijikstra(ll start, vector<array<ll, 2>> adjCheck[maxN + 1], ll dCheck[maxN + 1]){
	bool visited[maxN+1];
	for(int i = 1; i <= n; i++){
		visited[i] = false;
	}
	priority_queue <array<ll, 2> , vector<array<ll, 2>>,greater<array<ll, 2>>> pq;
	pq.push({0, start});
	while(!pq.empty()){
		array<ll, 2> cur = pq.top();
		pq.pop();
		if(visited[cur[1]]){
			continue;
		}
		dCheck[cur[1]] = cur[0];
		visited[cur[1]] = true;
		for(array<ll, 2> x: adjCheck[cur[1]]){
			if(!visited[x[0]] && cur[0] + x[1] < dCheck[x[0]]){
				dCheck[x[0]] = cur[0] + x[1];
				pq.push({cur[0] + x[1], x[0]});
			}
		}
	}
	return 0;
} 
 
int main() {
    cin >> n >> m;
	for(int i = 1; i <= n; i++){
		d[i] = maxV;
		d_back[i] = maxV;
	}
	d[1] = 0, d_back[n] = 0;
    for (int i = 1; i <= m; i++) {
		ll a, b, c;
		cin >> a >> b >> c;
        adj[a].push_back({b, c});
		adj_back[b].push_back({a, c});
    }
	dijikstra(1, adj, d);
	dijikstra(n, adj_back, d_back);
	ll ans = maxV;
	for(int i = 1; i <= n; i++){
		for(array<ll, 2> x: adj[i]){
			ans = min(ans, d[i] + d_back[x[0]] + x[1] / 2);
		}
	}
	cout << ans;
    return 0;
}
