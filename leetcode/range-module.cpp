#include <iostream>
#include<bits/stdc++.h>

using namespace std;

class RangeModule {
public:
    set<vector<int>> s;

    RangeModule() {

    }

    void addRange(int left, int right) {
        if (s.empty()) {
            s.insert({right, left});
            return;
        }
        auto it = s.lower_bound({left, 0});
        auto it2 = s.upper_bound({right, 0});
        if (it == s.end() || (*it)[1] > right) {
            s.insert({right, left});
            return;
        }
        int l, r;
        l = min((*it)[1], left);
        if (it2 != s.end() && (*it2)[1] <= right) {
            r = (*it2)[0];
            ++it2;
        } else {
            r = max(right, (*it)[0]);
        }
        s.erase(it, it2);
        s.insert({r, l});
        return;
    }

    bool queryRange(int left, int right) {
        if (s.empty()) {
            return false;
        }
        auto it = s.lower_bound({right, 0});
        return it != s.end() && (*it)[1] <= left;
    }

    void removeRange(int left, int right) {
        if (s.empty()) {
            return;
        }
        auto it = s.lower_bound({left, 0});
        auto it2 = s.upper_bound({right, 0});
        if (it == s.end() || (*it)[1] > right) {
            return;
        }
        int l1 = -1, r1 = -1, l2 = -1, r2 = -1;
        if (left > (*it)[1]) {
            l1 = (*it)[1];
            r1 = left;
        }
        if (it2 != s.end() && (*it2)[1] <= right) {
            l2 = right;
            r2 = (*it2)[0];
            ++it2;
        } else if (right < (*it)[0]) {
            l2 = right;
            r2 = (*it)[0];
        }
        s.erase(it, it2);
        if (l1 != -1 and r1 != -1) {
            s.insert({r1, l1});
        }
        if (l2 != -1 and r2 != -1) {
            s.insert({r2, l2});
        }
        return;
    }
};


int main() {
    RangeModule *obj = new RangeModule();
    obj->addRange(6, 8);
    obj->removeRange(7, 8);
    obj->removeRange(8, 9);
    obj->addRange(8, 9);
    obj->removeRange(1, 3);
    obj->addRange(1, 8);
    cout << obj->queryRange(2, 4);
    cout << obj->queryRange(2, 9);
    cout << obj->queryRange(4, 6);
    return 0;
}
