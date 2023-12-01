#include <iostream>
#include <cstdio>
#include <vector>
#include <limits>
#include <algorithm>
#include <set>
#include <unordered_set>
using namespace std;

int check(int index, string a) {
    if (index + 5 <= a.length()) {
        if (a.substr(index, 5) == "three") return 3;
        if (a.substr(index, 5) == "seven") return 7;
        if (a.substr(index, 5) == "eight") return 8;
    }
    if (index + 4 <= a.length()) {
        if (a.substr(index, 4) == "four") return 4;
        if (a.substr(index, 4) == "five") return 5;
        if (a.substr(index, 4) == "nine") return 9;
    }
    if (index + 3 <= a.length()) {
        if (a.substr(index, 3) == "one") return 1;
        if (a.substr(index, 3) == "two") return 2;
        if (a.substr(index, 3) == "six") return 6;
    }
    return 0;
}

int main(){
    freopen("1.in", "r", stdin);
    int sum = 0;
    for (int i = 0; i < 1000; i++) {
        int first = 0;
        int second = 0;
        string a;
        cin >> a;
        for (int i = 0; i < a.length(); i++) {
            if(a[i] < 58 || (first = check(i, a))) {
                if (first == 0) first = a[i] - '0';
                break;
            }
        }
        for (int i = a.length()-1; i > 0; i--) {
            if(a[i] < 58 || (second = check(i-1, a))) {
                if (second == 0) second = a[i] - '0';
                break;
            }
        }
        if (second == 0) second = first;
        sum += (first*10 + second);
    }

    cout << sum;
}