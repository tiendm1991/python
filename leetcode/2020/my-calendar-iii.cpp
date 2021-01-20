#include <iostream>
#include <set>
#include <iterator>
#include <vector>
#include <map>

using namespace std;

class MyCalendarThree {
public:
    map<int, int> s;

    MyCalendarThree() {}

    int book(int start, int end) {
        auto it = s.find(start);
        if (it != s.end()) {
            it->second += 1;
        } else {
            s.insert(pair<int, int>(start, 1));
        }
        it = s.find(end);
        if (it != s.end()) {
            it->second -= 1;
        } else {
            s.insert(pair<int, int>(end, -1));
        }
        int count = 0;
        int ans = 0;
        for (const auto &p : s) {
            count += p.second;
            if (count > ans) {
                ans = count;
            }
        }

        return ans;
    }
};

int main() {
    MyCalendarThree c;
    cout << c.book(10, 20);
    cout << c.book(50, 60);
    cout << c.book(10, 40);
    cout << c.book(5, 15);
    cout << c.book(5, 10);
    cout << c.book(25, 55);
    return 0;
}
