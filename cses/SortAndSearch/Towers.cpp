#include <iostream>
#include <bits/stdc++.h>
#include <set>
 
using namespace std;
 
const int maxN = 2e5;
int n, a[maxN];
 
int biSearch(int val, int left, int right){
    if(left > right){
        return -1;
    }
    if(a[left] > val){
        return left;
    }
    int mid = (left + right) / 2;
    if(a[mid] > val){
        return biSearch(val, left, mid);
    }else{
        return biSearch(val, mid+1, right);
    }
}
int main() {
    int count = 0;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        if (i == 0){
            a[i] = x;
            ++count;
            continue;
        }
        int j = biSearch(x, 0, count-1);
        if (j > -1){
            a[j] = x;
        }else{
            a[count++] = x;            
        }
    }
    
    cout << count;
    return 0;
}
