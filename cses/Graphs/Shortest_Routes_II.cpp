// Floyd–Warshall algorithm: https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
#include <iostream>
#include <bits/stdc++.h>
 
using namespace std;
#define ll long long
const int maxN = 500;
const ll maxV = 1e15;
ll d[maxN + 1][maxN + 1];
int n, m, q;
 
 
int main() {
    cin >> n >> m >> q;
	for(int i = 1; i <= n; i++){
		for(int j = 1; j <= n; j++){
			if(i == j){
				d[i][j] = 0;
			}else{
				d[i][j] = maxV;
			}
		}
	}
    for (int i = 1; i <= m; i++) {
		ll a, b, c;
		cin >> a >> b >> c;
        d[a][b] = min(d[a][b], c);
		d[b][a] = d[a][b];
    }
    //cout << "\n";
	for(int k = 1; k <= n; k++){
	    //cout << "\n";
		for(int i = 1; i <= n; i++){
			for(int j = 1; j <= n; j++){
				d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
			}
			//cout << d[i][j] << " ";
		}
	}
	//cout << "\n";
	for(int i = 0; i < q; i++){
		int x, y;
		cin >> x >> y;
		ll a = d[x][y] < maxV ? d[x][y] : -1;
		cout << a << "\n";
	}
    return 0;
}
