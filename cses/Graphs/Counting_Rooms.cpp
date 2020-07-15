#include <iostream>
#include <bits/stdc++.h>
 
using namespace std;
const int maxN = 1000;
int n, m;
string s[maxN];

bool valid(int i, int j){
	return 0 <= i && i < n && 0 <= j && j < m && s[i][j] == '.';
}

void dfs(int i, int j){
	s[i][j] = '#';
	if(valid(i-1, j)){
		dfs(i-1, j);
	}
	if(valid(i+1, j)){
		dfs(i+1, j);
	}
	if(valid(i, j-1)){
		dfs(i, j-1);
	}
	if(valid(i, j+1)){
		dfs(i, j+1);
	}
}

 
int main()
{
    cin >> n >> m;
	for(int i = 0; i < n; i++){
		cin >> s[i];
	}
	int ans = 0;
	for(int i = 0; i < n; i++){
		for(int j = 0; j < m; j++){
			if(s[i][j] == '.'){
				++ans;
				dfs(i, j);
			}
		}
	}
    cout << ans << endl;
}
