

// Bruteforce Approach
class Solution {
    public ArrayList<Integer> nextLargerElement(int[] arr) {
        // code here
        int n = arr.length;
        ArrayList<Integer> result = new ArrayList<>();
        
        for (int i = 0; i< n;i++){
            int nxtgreater = -1;
            for (int j = i + 1; j< n ; j++){
                if (arr[j] > arr [i]){
                    nxtgreater = arr[j];
                    break;
                }
            }
            result.add(nxtgreater);
            
        }
        return result;
        
    }
}
