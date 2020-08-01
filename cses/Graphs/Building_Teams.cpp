#include <iostream>
#include <bits/stdc++.h>
 
using namespace std;
#define ll long long
const int maxN = 1e5, maxM = 2e5;
int a[maxN + 1], ans[maxN + 1];
bool visited[maxN+1];
vector<int> adj[maxN + 1];
int n, m;

bool dfs(int v, int g){
	if(visited[v]){
		return ans[v] == g;
	}
	visited[v] = true;
	ans[v] = g;
	for(int i : adj[v]){
		if(!dfs(i, 3-g)){
			return false;
		}
	}
	return true;
}

int main() {
    cin >> n >> m;
    for (int i = 1; i <= m; i++) {
		int a, b;
		cin >> a >> b;
        adj[a].push_back(b);
		adj[b].push_back(a);
    }
	
    for(int i = 1; i<= n; i++){
		if(!visited[i] && !dfs(i, 1)){
			cout << "IMPOSSIBLE";
			return 0;
		}
	}
	for(int i = 1; i<= n; i++){
		cout << ans[i] << " ";
	}
    return 0;
}
