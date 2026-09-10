class Solution {
    public static int largest(int[] arr) {
        // code here
        int large = 0;
        for(int i=0; i<=arr.length-1; i++){
            if(large < arr[i]){
                large = arr[i];
            }
        }
        return large;
    }
}
