#include <iostream>
#include <array>
#include <vector>

using namespace std;
#define ll long long
#define ar array
const int maxN = 1e3;
ll dp[maxN + 1][maxN + 1];
string s[maxN];
int n, q;

int main() {
    cin >> n >> q;
    for (int i = 1; i <= n; i++) {
        cin >> s[i - 1];
        for (int j = 1; j <= n; j++) {
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1];
            if (s[i - 1][j - 1] == '*') {
                dp[i][j] += 1;
            }
        }
    }
    for (int i = 0; i < q; i++) {
        int y1, x1, y2, x2;
        cin >> y1 >> x1 >> y2 >> x2;
        cout << dp[y2][x2] - dp[y1 - 1][x2] - dp[y2][x1 - 1] + dp[y1 - 1][x1 - 1] << "\n";
    }
    return 0;
}
