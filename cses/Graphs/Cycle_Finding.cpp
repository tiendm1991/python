https://cp-algorithms.com/graph/finding-negative-cycle-in-graph.html#toc-tgt-0
#include <iostream>
#include <bits/stdc++.h>
 
using namespace std;
#define ll long long
#define arr3 array<int, 3>
 
const int maxN = 2500, maxM = 5e3;
const ll maxV = 1e18;
int n, m;
int par[maxN + 1];
ll dist[maxN + 1];
arr3 edges[maxM + 1];
 
int main() {
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        edges[i] = {a, b, c};
    }
    for (int i = 1; i <= n; i++) {
        dist[i] = maxV;
    }
    for (int i = 1; i < n; i++) {
        for (arr3 e: edges) {
            if (dist[e[1]] > dist[e[0]] + e[2]) {
                dist[e[1]] = dist[e[0]] + e[2];
                par[e[1]] = e[0];
            }
        }
    }
    int startCycle = -1;
    for (arr3 e: edges) {
        if (dist[e[1]] > dist[e[0]] + e[2]) {
            startCycle = e[1];
            break;
        }
    }
    if (startCycle == -1) {
        cout << "NO";
    } else {
        cout << "YES\n";
        set<int> trace;
        while(trace.find(startCycle) == trace.end()){
            trace.insert(startCycle);
            startCycle = par[startCycle];
        }
        stack<int> s;
        s.push(startCycle);
        int cur = par[startCycle];
        while(cur != startCycle){
            s.push(cur);
            cur = par[cur];
        }
        s.push(startCycle);
        while (!s.empty()){
            cout << s.top() << " ";
            s.pop();
        }
    }
    return 0;
}
