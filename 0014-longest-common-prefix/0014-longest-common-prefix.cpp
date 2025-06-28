class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
         if (strs.empty()) {
            return "";
        }
        sort(strs.begin(), strs.end());
        string first = strs[0];
        string last = strs[strs.size() - 1];
        string ans = "";
        for (size_t i = 0; i < min(first.length(), last.length()); ++i) {
            if (first[i] != last[i]) {
                return ans;
            }
            ans += first[i];
        }
        return ans;
    }
};