class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        auto n = nums.size();
        unordered_map<int, int> frequencies;
        for(auto num : nums){
            ++frequencies[num];
        }

        vector<vector<int>> bucket(n + 1);
        for(auto const& [num, frequency] : frequencies){
            bucket[frequency].emplace_back(num);
        }

        vector<int> ans;
        ans.reserve(k);
        for(int frequency = n; frequency >= 0; --frequency){
            for(auto num : bucket[frequency]){
                ans.push_back(num);
                if(k == ans.size()){
                    return ans;
                }
            }
        }
    }
};
