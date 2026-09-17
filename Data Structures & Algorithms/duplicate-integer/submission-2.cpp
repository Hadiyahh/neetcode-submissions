class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        for (int i=0; i < nums.size() ; i++)
        {
            if (seen.find(nums[i]) != seen.end()) // Tgis line is stating that it has been seen 
            {
                return true; 
            } else if (seen.find(nums[i])== seen.end()) {
                seen.insert(nums[i]);
            }
        }
            return false; // No duplicates 
    }
};



