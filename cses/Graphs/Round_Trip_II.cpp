#include <iostream>
#include <vector>
#include <stack>
 
using namespace std;
#define ll long long
const int maxN = 1e5, maxM = 2e5;
int visited[maxN+1], p[maxN+1];
vector<int> edges[maxN + 1];
int n, m;
 
int dfs(int v, int u){
    p[v] = u;
    if(visited[v] == 1){
        return v;
    }
    if(visited[v] == 2){
        return 0;
    }
    visited[v] = 1;
    p[v] = u;
    for(auto i : edges[v]){
        int s = dfs(i, v);
        if(s != 0){
            return s;
        }
    }
    visited[v] = 2;
    return 0;
}
int main() {
    cin >> n >> m;
    for (int i = 1; i <= m; i++) {
        int a, b;
        cin >> a >> b;
        edges[a].push_back(b);
    }
    for(int v = 1; v <= n; v++){
        int startCycle = dfs(v, 0);
        if(startCycle != 0){
            stack<int> s;
            s.push(startCycle);
            int cur = p[startCycle];
            while(cur != startCycle){
                s.push(cur);
                cur = p[cur];
            }
            s.push(startCycle);
            cout << s.size() << "\n";
            while(!s.empty()){
                cout << s.top() << " ";
                s.pop();
            }
            return 0;
        }
    }
    cout << "IMPOSSIBLE";
    return 0;
}
