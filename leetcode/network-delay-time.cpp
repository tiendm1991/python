#include <iostream>
#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<int>> edges[101];
    int d[101];
    const int MAX_INT = 1e6;

    int networkDelayTime(vector<vector<int>> &times, int N, int K) {
        for (int i = 1; i <= N; i++) {
            d[i] = MAX_INT;
        }
        for (vector<int> t: times) {
            edges[t[0]].push_back({t[2], t[1]});
        }
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> q;
        q.push({0, K});

        while (!q.empty()) {
            vector<int> x = q.top();
            q.pop();
            if (x[0] < d[x[1]]) {
                d[x[1]] = x[0];
            }
            for (vector<int> v: edges[x[1]]) {
                if (x[0] + v[0] < d[v[1]]) {
                    q.push({x[0] + v[0], v[1]});
                }
            }
        }
        int ans = 0;
        for (int i = 1; i <= N; i++) {
            if (d[i] >= MAX_INT) {
                return -1;
            } else if (d[i] > ans) {
                ans = d[i];
            }

        }
        return ans;
    }
};

int main() {
    Solution s;
    vector<vector<int>> times;
    times.push_back({1, 2, 1});
    times.push_back({2, 3, 2});
    times.push_back({1, 3, 2});
    cout << s.networkDelayTime(times, 3, 1);
    return 0;
}
