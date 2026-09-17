class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> hashMap;

    for (int i = 0; i < nums.size(); i++){
        int n = target - nums[i];
        if (hashMap.find(n) != hashMap.end()) { // Meaning if its been found 
            // Then we need to find that number in our array 
            return {hashMap[n],i};
        }
        hashMap[nums[i]] = i;
    }
        }
};

// Target subtract the numbers in the array then we have to find it 
// In C++ we dont have a hashmap we have a unordered set

