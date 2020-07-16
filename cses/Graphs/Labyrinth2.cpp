#include <algorithm>
#include <iostream>
#include <vector>
#include <tuple>
#include <queue>
 
#define pairs array<int, 2>
 
using namespace std;
 
const int maxN = 1000;
int n, m;
string s[maxN];
 
bool valid(int i, int j) {
    return 0 <= i && i < n && 0 <= j && j < m && s[i][j] != '#';
}
 
int main() {
    int ai, aj, bi, bj;
    cin >> n >> m;
    char trace[n][m];
    for (int i = 0; i < n; i++) {
        cin >> s[i];
        for (int j = 0; j < m; j++) {
            trace[i][j] = '.';
            if (s[i][j] == 'A') {
                ai = i, aj = j;
            }
            if (s[i][j] == 'B') {
                bi = i, bj = j;
            }
        }
    }
 
    queue<pairs > q;
    pairs target = {bi, bj};
    pairs source = {ai, aj};
    q.push(source);
    string ans = "";
    while (!q.empty()) {
        pairs current = q.front();
        q.pop();
        int i = current[0], j = current[1];
        if (current == target) {
            break;
        }
        if (valid(i - 1, j)) {
            q.push({i - 1, j});
            trace[i - 1][j] = 'U';
        }
        if (valid(i + 1, j)) {
            q.push({i + 1, j});
            trace[i + 1][j] = 'D';
        }
        if (valid(i, j - 1)) {
            q.push({i, j - 1});
            trace[i][j - 1] = 'L';
        }
        if (valid(i, j + 1)) {
            q.push({i, j + 1});
            trace[i][j + 1] = 'R';
        }
        s[i][j] = '#';
    }
    if (trace[bi][bj] == '.') {
        cout << "NO" << "\n";
    } else {
        int i = bi, j = bj;
        while (i != ai || j != aj) {
            ans.push_back(trace[i][j]);
            if (trace[i][j] == 'U') {
                i++;
                continue;
            }
			if (trace[i][j] == 'D') {
                i--;
                continue;
            } 
			if (trace[i][j] == 'L') {
                j++;
                continue;
            } 
			if (trace[i][j] == 'R') {
                j--;
                continue;
            }
        }
        reverse(ans.begin(), ans.end());
        cout << "YES" << "\n";
        cout << ans.length() << "\n";
        cout << ans << endl;
    }
}
