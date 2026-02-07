class Solution {
    public int minimumDeletions(String s) {
        int b = 0;
        int ans = 0;
        for(int i = 0; i< s.length();i++){
            char ch = s.charAt(i);
            if (ch == 'b'){
                b++;
            } else {
                ans++;
                ans = Math.min(ans,b);
            }
        }
        return ans;
    }
}
