class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    rob(nums) {

        const memo = {}

        const getMoney = (i) =>{

            if (memo.hasOwnProperty(i)) {
                return memo[i];
            }

            if (i >= nums.length){
                return 0;
            }

            memo [i] = Math.max(getMoney(i+1), nums[i]+ getMoney(i+2));     
            return memo[i];
        }

        return getMoney(0);
    }
}
