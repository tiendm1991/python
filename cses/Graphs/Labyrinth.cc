#include<bits/stdc++.h>
 
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
    map<pair<int, int>, pair<pair<int, int>, char>> trace;
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
    }
 
    queue<pair<int, int> > q;
    pair<int, int> target = make_pair(bi, bj);
    pair<int, int> source = make_pair(ai, aj);
    q.push(source);
    string ans = "";
    while (!q.empty()) {
        pair<int, int> current = q.front();
        q.pop();
        int i = current.first, j = current.second;
        if (current == target) {
            while (current != source) {
                pair<pair<int, int>, char> parent = trace[current];
                ans.push_back(parent.second);
                current = parent.first;
            }
            reverse(ans.begin(), ans.end());
            cout << "YES" << "\n";
            cout << ans.length() << "\n";
            cout << ans << endl;
            return 0;
        }
        if (valid(i - 1, j)) {
            pair<int, int> a = make_pair(i - 1, j);
            q.push(a);
            trace[a] = make_pair(current, 'U');
        }
        if (valid(i + 1, j)) {
            pair<int, int> a = make_pair(i + 1, j);
            q.push(a);
            trace[a] = make_pair(current, 'D');
        }
        if (valid(i, j - 1)) {
            pair<int, int> a = make_pair(i, j - 1);
            q.push(a);
            trace[a] = make_pair(current, 'L');
        }
        if (valid(i, j + 1)) {
            pair<int, int> a = make_pair(i, j + 1);
            q.push(a);
            trace[a] = make_pair(current, 'R');
        }
        s[i][j] = '#';
    }
    cout << "NO" << "\n";

}
