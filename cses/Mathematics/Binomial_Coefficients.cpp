#include <iostream>
#include <array>
#include <vector>

using namespace std;
#define ll long long
#define ar array
const ll mod = 1e9 + 7, maxV = 1e6;
ll f[maxV + 1], inv[maxV + 1], f_inv[maxV + 1];
int n;

int main() {
    f[0] = 1;
    for (int i = 1; i <= maxV; i++) {
        f[i] = (f[i - 1] * i) % mod;
    }
    inv[1] = 1;
    for (int i = 2; i <= maxV; ++i) {
        inv[i] = mod - (mod / i) * inv[mod % i] % mod;
    }
    f_inv[0] = 1;
    for (int i = 1; i <= maxV; i++) {
        f_inv[i] = f_inv[i - 1] * inv[i] % mod;
    }
    cin >> n;
    for (int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;
        if (b == 0 || b == a) {
            cout << 1 << "\n";
        }else{
            cout << (f[a] * (f_inv[b] * f_inv[a - b] % mod)) % mod << "\n";
        }
    }
    return 0;
}
