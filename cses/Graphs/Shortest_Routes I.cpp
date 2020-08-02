#include <iostream>
#include <bits/stdc++.h>
 
using namespace std;
#define ll long long
const int maxN = 1e5;
const ll maxV = 1e15;
ll a[maxN + 1], ans[maxN + 1];
bool visited[maxN+1];
vector<array<ll, 2>> adj[maxN + 1];
int n, m;


int main() {
    cin >> n >> m;
	for(int i = 2; i <= n; i++){
		ans[i] = maxV;
	}
    for (int i = 1; i <= m; i++) {
		int a, b, c;
		cin >> a >> b >> c;
        adj[a].push_back({b, c});
    }
	//min heap
	priority_queue <array<ll, 2> , vector<array<ll, 2>>,greater<array<ll, 2>>> pq;
	pq.push({0, 1});
	while(!pq.empty()){
		array<ll, 2> cur = pq.top();
		pq.pop();
		if(visited[cur[1]]){
			continue;
		}
		ans[cur[1]] = cur[0];
		visited[cur[1]] = true;
		for(array<ll, 2> x: adj[cur[1]]){
			if(!visited[x[0]]){
				pq.push({cur[0] + x[1], x[0]});
			}
		}
	}
	for(int i = 1; i <= n; i++){
		cout << ans[i] << " ";
	}
    return 0;
}
