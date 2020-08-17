#include <iostream>
#include <vector>
#include <math.h>
 
using namespace std;
#define ll long long
const int maxA = 1e6;
int a[maxA + 1];
int n;
 
bool isCommonDiv(int x) {
    int d = 0;
    for (int i = 0; i <= maxA; i += x) {
        if (a[i] > 0) {
            ++d;
            if (a[i] >= 2 || d == 2){
                return true;
            }
        }
    }
    return false;
}
 
int main() {
    cin >> n;
    int maxAns = 0;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        a[x]++;
    }
    for (int x = maxA; x > 0; x--) {
        if (isCommonDiv(x)) {
            cout << x;
            return 0;
        }
    }
    return 0;
}
