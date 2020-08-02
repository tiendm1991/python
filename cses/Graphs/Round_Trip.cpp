#include <iostream>
#include <bits/stdc++.h>
 
using namespace std;
#define ll long long
const int maxN = 1e5, maxM = 2e5;
int a[maxN + 1], p[maxN + 1];
bool visited[maxN+1];
vector<int> adj[maxN + 1];
int n, m;


bool dfs(int v, int u){
	visited[v] = true;
	p[v] = u;
	for(int w : adj[v]){
		if(!visited[w]){
			if(dfs(w, v)){
				return true;
			}
		}else if(w != u) {
			int cur = v;
			int s = 2;
			while(cur != w){
				++s;
				cur = p[cur];
			}
			cout << s << "\n";
			cout << w;
			cur = v;
			while(cur != w){
				cout << " " << cur;
				cur = p[cur];
			}
			cout << " " << w;
			return true;
		}
	}
	return false;
}

int main() {
    cin >> n >> m;
    for (int i = 1; i <= m; i++) {
		int a, b;
		cin >> a >> b;
        adj[a].push_back(b);
		adj[b].push_back(a);
    }
	for(int i = 1; i <= n; i++){
		if(!visited[i]){
			if(dfs(i, 0)){
				return 0;
			}
		}
	}
    cout << "IMPOSSIBLE";
    return 0;
}
