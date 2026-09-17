#include <array>
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> hashMap;
        for (const string& str : strs){

            array<int,26> freq = {0};

            for (char c : str){
                freq[c-'a']++;
            }
            string key = "";
            for (int count : freq){
                key+= to_string(count)+'#';
            }
        
            hashMap[key].push_back(str);
        }
            vector<vector<string>> result;
            for ( const auto&entry : hashMap ){
                result.push_back(entry.second);
            }
            return result;
        }

};


