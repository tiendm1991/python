#include <iostream>
#include <bits/stdc++.h>

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
    map<char, pair<int, int>> direct;
    direct['U'] = make_pair(1, 0);
    direct['D'] = make_pair(-1, 0);
    direct['L'] = make_pair(0, 1);
    direct['R'] = make_pair(0, -1);

    queue<pairs > q;
    pairs target = {bi, bj};
    pairs source = {ai, aj};
    q.push(source);
    string ans = "";
    s[ai][aj] = '#';
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
            s[i - 1][j] = '#';
        }
        if (valid(i + 1, j)) {
            q.push({i + 1, j});
            trace[i + 1][j] = 'D';
            s[i + 1][j] = '#';
        }
        if (valid(i, j - 1)) {
            q.push({i, j - 1});
            trace[i][j - 1] = 'L';
            s[i][j - 1] = '#';
        }
        if (valid(i, j + 1)) {
            q.push({i, j + 1});
            trace[i][j + 1] = 'R';
            s[i][j + 1] = '#';
        }
    }
    if (trace[bi][bj] == '.') {
        cout << "NO" << "\n";
    } else {
        while (bi != ai || bj != aj) {
            ans.push_back(trace[bi][bj]);
            pair<int, int> next = direct[trace[bi][bj]];
            bi += next.first;
            bj += next.second;
        }
        reverse(ans.begin(), ans.end());
        cout << "YES" << "\n";
        cout << ans.length() << "\n";
        cout << ans << endl;
    }
}
