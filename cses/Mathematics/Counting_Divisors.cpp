#include <iostream>
#include <vector>
#include <math.h>

using namespace std;
#define ll long long
const int maxN = 1e5, maxX = 1e6;
ll d[maxX + 1];
int n;


int main() {
    cin >> n;
    for (int i = 2; i <= maxX; i++) {
        d[i] = 2;
    }
    d[1] = 1;
    int maxloop = sqrt(maxX);
    for (int i = 2; i <= maxloop; i++) {
        int j = i;
        ll u = i * j;
        while (u <= maxX) {
            if (i == j) {
                d[u] += 1;
            } else {
                d[u] += 2;
            }
            j++;
            u = i * j;
        }
    }

    for (int i = 1; i <= n; i++) {
        int x;
        cin >> x;
        cout << d[x] << "\n";
    }

    return 0;
}
