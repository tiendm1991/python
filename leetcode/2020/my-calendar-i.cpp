#include <iostream>
#include <set>
#include <iterator>
#include <vector>
#include <map>

using namespace std;

class MyCalendar {
public:
    set<vector<int>> s;

    MyCalendar() {

    }

    bool book(int start, int end) {
        if (s.empty()) {
            s.insert({start, end});
            return true;
        }
        if ((*s.rbegin())[1] <= start || (*s.begin())[0] >= end) {
            s.insert({start, end});
            return true;
        }
        auto v = s.lower_bound({end, end});
        --v;
        if ((*v)[1] <= start) {
            s.insert({start, end});
            return true;
        }
        return false;
    }
};

int main() {
    MyCalendar c;
    cout << c.book(10, 20);
    cout << c.book(50, 60);
    cout << c.book(10, 40);
    cout << c.book(5, 15);
    cout << c.book(5, 10);
    cout << c.book(25, 55);
    return 0;
}
