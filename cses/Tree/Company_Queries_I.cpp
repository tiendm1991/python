#include <iostream>
#include <vector>


using namespace std;
const int maxN = 2e5;
int n, q, a[maxN + 1], tree[maxN + 1][20];

int main() {
    cin >> n >> q;
    for (int i = 2; i <= n; i++) {
        cin >> a[i];
    }
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < 20; j++) {
            if (j == 0) {
                tree[i][j] = a[i];
            } else {
                if (tree[tree[i][j - 1]][j - 1] == 0) {
                    break;
                } else {
                    tree[i][j] = tree[tree[i][j - 1]][j - 1];
                }
            }
        }
    }
    for (int i = 0; i < q; i++) {
        int x, k;
        cin >> x >> k;
        int j = 0;
        while (k > 0) {
            if (k % 2 == 1) {
                x = tree[x][j];
                if (x == 0) {
                    x = -1;
                    break;
                }
            }
            j++;
            k /= 2;
        }
        cout << x << "\n";
    }
    return 0;
}
