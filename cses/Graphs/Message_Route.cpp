#include <iostream>
#include <bits/stdc++.h>
 
using namespace std;
#define ll long long
const int maxN = 1e5, maxM = 2e5;
int a[maxN + 1], p[maxN + 1];
bool visited[maxN+1];
vector<int> adj[maxN + 1];
int n, m;

int main() {
    cin >> n >> m;
    for (int i = 1; i <= m; i++) {
		int a, b;
		cin >> a >> b;
        adj[a].push_back(b);
		adj[b].push_back(a);
    }
    queue<int> q;
	q.push(1);
	visited[1] = true;
	while(!q.empty()){
		int cur = q.front();
		q.pop();
		if(cur == n){
			stack<int> ans;
			while(cur != 0){
				ans.push(cur);
				cur = p[cur];
			}
			cout << ans.size() << "\n";
			while(!ans.empty()){
			    cout << ans.top() << " ";
			    ans.pop();
			}
			return 0;
		}
		for(int i : adj[cur]){
			if(!visited[i]){
				q.push(i);
				visited[i] = true;
				p[i] = cur;
			}
		}
	}
    cout << "IMPOSSIBLE";
    return 0;
}
