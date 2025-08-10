class Solution {
public:
    string frequencySort(string s) {
        sort(s.begin(),s.end());
         priority_queue<pair<int, char>> pq;
         int count=1;
         for(int i=1; i<s.size(); i++){
            if(s[i]==s[i-1]){
                count++;
            }
            else{
                pq.push({count,s[i-1]});
                count=1;
            }
         }
         pq.push({count,s[s.size()-1]});
        int j=0;
         while(!pq.empty()){
            for(int i=0; i<pq.top().first; i++){
                s[j++]=pq.top().second;
            }
            pq.pop();
         }
         return s;
    }
};