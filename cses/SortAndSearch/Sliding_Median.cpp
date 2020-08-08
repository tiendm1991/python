#include <iostream>
#include <bits/stdc++.h>
 
using namespace std;
#define ll long long
#define arr2 array<int, 2>
 
const ll maxN = 2e5;
multiset<ll> minHeap, maxHeap;
ll n, k, a[maxN];
 
void resize() {
    if (minHeap.size() > maxHeap.size()) {
        auto it = minHeap.begin();
        maxHeap.insert(-(*it));
        minHeap.erase(it);
    } else if (maxHeap.size() - minHeap.size() > 1) {
        auto it = maxHeap.begin();
        minHeap.insert(-(*it));
        maxHeap.erase(it);
    }
}
 
void add(int x) {
    if (minHeap.size() == 0 && maxHeap.size() == 0) {
        minHeap.insert(x);
    } else if (minHeap.size() > 0 && x >= *minHeap.begin()) {
        minHeap.insert(x);
    } else {
        maxHeap.insert(-x);
    }
    resize();
}
 
void remove(int x) {
    if (x >= *minHeap.begin()) {
		auto it = minHeap.find(x);
        minHeap.erase(it);
    } else {
		auto it = maxHeap.find(-x);
        maxHeap.erase(it);
    }
    resize();
}
 
int getMedian() {
    return -(*maxHeap.begin());
}
 
int main() {
    cin >> n >> k;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    if (k == 1) {
        for (int i = 0; i < n; i++) {
            cout << a[i] << " ";
        }
        return 0;
    }
 
    for (int i = 0; i < k - 1; i++) {
        add(a[i]);
    }
    for (int i = k - 1; i < n; i++) {
        add(a[i]);
        cout << getMedian() << " ";
        remove(a[i - k + 1]);
    }
    return 0;
}
