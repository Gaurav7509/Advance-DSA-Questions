class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] answer = new int[n];
        Arrays.fill(answer,1);
        int p = 1;
        for(int i = 0; i<n; i++){
            answer[i] = p;
            p = p * nums[i];
        }
        int s = 1;
        for(int i = n-1; i>=0; i--){
            answer[i] = answer[i]* s;
            s= s*nums[i];
        }
        return answer;
        
    }
}
