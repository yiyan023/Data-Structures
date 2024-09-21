#include <cctype>   // for isalnum and tolower
#include <string>   // for string class

class Solution {
public:
    bool isPalindrome(std::string s) {
        int l = 0;
        int r = s.size()-1;

        while (l < r) {
            if (!isalnum(s[l])) {
                l += 1;
                continue;
            } if (!isalnum(s[r])) {
                r -= 1;
                continue;
            } if (tolower(s[l]) != tolower(s[r])) {
                return false;
            } else {
                l += 1;
                r -= 1;
            }
        }

        return true;
    }
};