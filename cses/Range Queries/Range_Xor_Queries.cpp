#include <iostream>
#include <bits/stdc++.h>

using namespace std;
#define ll long long
#define ar array
const int maxN = 2 * 1e5, maxInt = 1e9;
int a[maxN];
ll st[4 * maxN];
int n, q;

void update(int id, int left, int right, int i, int val){
	if(i < left || i > right){
		return;
	}
	if(left == right){
		st[id] = val;
		return;
	}
	int mid = (left + right) / 2;
	update(id * 2 + 1, left, mid, i, val);
    update(id * 2 + 2, mid + 1, right, i, val);
    st[id] = st[id * 2 + 1] ^ st[id * 2 + 2];
}

int getXor(int id, int left, int right, int u, int v){
	if(v < left || u > right){
		return 0;
	}
	if(u <= left && v >= right){
		return st[id];
	}
	int mid = (left + right) / 2;
    return getXor(id * 2 + 1, left, mid, u, v) ^ getXor(id * 2 + 2, mid + 1, right, u, v);
}

int main()
{
    cin >> n >> q;
    for (int i = 0; i < n; i++)
        cin >> a[i];
    for(int i = 0; i < n; i++){
    	update(0, 0, n-1, i, a[i]);
    }
    int left, right;
    for(int i = 0; i < q; i++){
    	cin >> left >> right;
    	cout << getXor(0, 0, n-1, left - 1, right - 1) << "\n";
    }

}
