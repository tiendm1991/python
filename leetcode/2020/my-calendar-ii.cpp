#include <iostream>
#include <set>
#include <iterator>
#include <vector>
#include <map>

using namespace std;

class MyCalendarTwo {
public:
    map<int, int> s;

    MyCalendarTwo() {

    }

    bool book(int start, int end) {
        if (s.empty()) {
            s.insert(pair<int, int>(start, 1));
            s.insert(pair<int, int>(end, -1));
            return true;
        }
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
        for (const auto &p : s) {
            count += p.second;
            if (count == 3) {
                it = s.find(start);
                it->second -= 1;
                it = s.find(end);
                it->second += 1;
                return false;
            }
        }

        return true;
    }
};


int main() {
    MyCalendarTwo c;
    cout << c.book(10, 20);
    cout << c.book(50, 60);
    cout << c.book(10, 40);
    cout << c.book(5, 15);
    cout << c.book(5, 10);
    cout << c.book(25, 55);
    return 0;
}
