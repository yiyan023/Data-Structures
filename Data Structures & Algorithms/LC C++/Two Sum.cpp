#include <vector>
#include <unordered_map>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::unordered_map<int, int> hash;

        for (int i = 0; i < nums.size(); ++i) {
            int num = nums[i];
            int complement = target - num;

            if (hash.find(complement) != hash.end()) {
                return {hash[complement], i};
            } else {
                hash[num] = i;
            }
        }

        return {};
    }
};
