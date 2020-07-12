#include <iostream>
#include <bits/stdc++.h>
 
using namespace std;
bool visited[7][7];
string s;
int result;

void dfs(int i, int j, int step, char m){
    if (i == 6 && j == 0){
        if (step == 48){
            ++result;
        }
        return;
    }
    char ch = s[step];
    if (m == 'L' && (j == 0 || visited[i][j-1]) && i > 0 && i < 6 && !visited[i-1][j] && !visited[i+1][j]) return;
    if (m == 'R' && (j == 6 || visited[i][j+1]) && i > 0 && i < 6 && !visited[i-1][j] && !visited[i+1][j]) return;
    if (m == 'U' && (i == 0 || visited[i-1][j]) && j > 0 && j < 6 && !visited[i][j-1] && !visited[i][j+1]) return;
    if (m == 'D' && (i == 6 || visited[i+1][j]) && j > 0 && j < 6 && !visited[i][j-1] && !visited[i][j+1]) return;
    visited[i][j] = true;
    if (ch == '?' || ch == 'D'){
        if (i < 6 && !visited[i+1][j]){
            dfs(i+1, j, step+1, 'D');
        }
    }
    if (ch == '?' || ch == 'U'){
        if (i > 0 && !visited[i-1][j]){
            dfs(i-1, j, step+1, 'U');
        }
    }
    if (ch == '?' || ch == 'L'){
        if (j > 0 && !visited[i][j-1]){
            dfs(i, j-1, step+1, 'L');
        }
    }
    if (ch == '?' || ch == 'R'){
        if (j < 6 && !visited[i][j+1]){
            dfs(i, j+1, step+1, 'R');
        }
    }
    visited[i][j] = false;
}
 
int main()
{
    cin >> s;
    dfs(0, 0, 0, '.');
    cout << result << endl;
}