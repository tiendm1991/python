#include <iostream>
#include <array>
#include <set>

using namespace std;
#define ll long long
#define arr2 array<int, 2>

const ll maxN = 2e5;
set<arr2 > minHeap, maxHeap;
int n, k, s, a[maxN];

int add(int x) {
    int s1 = minHeap.size(), s2 = maxHeap.size();
    if (k % 2 == 0) {

    } else {

    }
}

int remove(int x) {

}

int getMedian() {

}

int main() {
    cin >> n >> k;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    for (int i = 1; i < k; i++) {
        add(a[i]);
    }
    for (int i = k; i < n; i++) {
        add(a[i]);
        cout << getMedian() << " ";
        remove(a[i - k]);
    }
    return 0;
}
