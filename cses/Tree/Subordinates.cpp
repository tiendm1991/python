#include <iostream>
#include <vector>

using namespace std;
#define ll long long
const int maxN = 2e5;
int d[maxN + 1];
bool visited[maxN+1];
vector<int> adj[maxN + 1];
int n, m;

int dfs(int u){
    visited[u] = true;
    int ans = 0;
    for(int v: adj[u]){
        if(!visited[v]){
            ans += 1 + dfs(v);
        }
    }
    d[u] = ans;
    return d[u];
}

int main() {
    cin >> n;
	for(int i = 2; i <= n; i++){
        int x;
        cin >> x;
        adj[x].push_back(i);
    }

	for(int i = 1; i <= n; i++){
		if(!visited[i]){
		    dfs(i);
		}
	}

	for(int i = 1; i<= n; i++){
	    cout << d[i] << " ";
	}
    return 0;
}
