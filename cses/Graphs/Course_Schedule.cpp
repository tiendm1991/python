#include <iostream>
#include <bits/stdc++.h>
 
using namespace std;
#define ll long long
const int maxN = 1e5, maxM = 2e5;
int a[maxN + 1], visited[maxN+1];
vector<int> require[maxN + 1], ans;
int n, m;
 
bool dfs(int v){
	if(visited[v] != 0){
		return visited[v] == 2;
	}
	visited[v] = 1;
	for(auto i : require[v]){
		if(!dfs(i)){
			return false;
		}
	}
	ans.push_back(v);
	visited[v] = 2;
	return true;
}
int main() {
    cin >> n >> m;
    for (int i = 1; i <= m; i++) {
		int a, b;
		cin >> a >> b;
        require[b].push_back(a);
    }
	for(int v = 1; v <= n; v++){
		if(!dfs(v)){
			cout << "IMPOSSIBLE";
			return 0;
		}
	}
	for(auto x : ans){
		cout << x << " ";
	}
    return 0;
}
