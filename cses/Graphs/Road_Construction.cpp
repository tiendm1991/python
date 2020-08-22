#include <iostream>
#include <array>

using namespace std;

const int maxN = 1e5;
int p[maxN + 1], s[maxN + 1];
int n, m, maxSize = 1;

int find(int u) {
    while (u != p[u]) {
        u = p[u];
    }
    return u;
}

void unions(int ru, int rv) {
    int r = min(ru, rv), c = max(ru, rv);
    p[c] = r;
    s[r] += s[c];
    maxSize = max(maxSize, s[r]);
}

int main() {
    cin >> n >> m;

    for (int i = 1; i <= n; i++) {
        p[i] = i;
        s[i] = 1;
    }

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        int ra = find(a), rb = find(b);
        if (ra == rb) {
            cout << n << " " << maxSize << "\n";
        } else {
            unions(ra, rb);
            cout << --n << " " << maxSize << "\n";
        }
    }
    return 0;
}
