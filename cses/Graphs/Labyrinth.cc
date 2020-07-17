#include <iostream>
#include <bits/stdc++.h>

#define pairs array<int, 2>

using namespace std;

const int maxN = 1000, di[4] = {1, 0, -1, 0}, dj[4] = {0, 1, 0, -1};
char dc[4] = {'D', 'R', 'U', 'L'};
int n, m, d[maxN][maxN];
string s[maxN], p[maxN];

bool valid(int i, int j) {
    return 0 <= i && i < n && 0 <= j && j < m && s[i][j] != '#';
}

int main() {
    int ai, aj, bi, bj;
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        cin >> s[i];
        for (int j = 0; j < m; j++) {
            if (s[i][j] == 'A') {
                ai = i, aj = j;
            }
            if (s[i][j] == 'B') {
                bi = i, bj = j;
            }
        }
        p[i] = string(m, 0);
    }

    queue<pairs > q;
    pairs target = {bi, bj};
    pairs source = {ai, aj};
    q.push(source);
    while (!q.empty()) {
        pairs current = q.front();
        q.pop();
        int i = current[0], j = current[1], k = current[2];
        if (current == target) {
            break;
        }
        for (int k = 0; k < 4; k++) {
            int ni = current[0] + di[k], nj = current[1] + dj[k];
            if (valid(ni, nj)) {
                q.push({ni, nj});
                s[ni][nj] = '#';
                p[ni][nj] = dc[k];
                d[ni][nj] = k;
            }
        }
        s[i][j] = '#';
    }
    if (!p[bi][bj]) {
        cout << "NO" << "\n";
    } else {
        string ans;
        while (bi != ai || bj != aj) {
            ans.push_back(p[bi][bj]);
            // int dd = d[bi][bj] ^ 2; // 0->2, 2->0, 1->3, 3->1
            int dd = 2 - d[bi][bj];
            if (d[bi][bj] % 2 == 1) {
                dd = 4 - d[bi][bj];
            }
            bi += di[dd];
            bj += dj[dd];
        }
        reverse(ans.begin(), ans.end());
        cout << "YES" << "\n";
        cout << ans.length() << "\n";
        cout << ans << endl;
    }
}
