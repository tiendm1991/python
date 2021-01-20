import java.lang.reflect.Array;
import java.util.*;
import java.util.logging.Level;
import java.util.stream.Collectors;

class Solution {
    public int minimumMountainRemovals(int[] nums) {
        int res = 0;
        int[] dp1 = new int[nums.length];
        TreeSet<Integer> t = new TreeSet<>();
        t.add(nums[0]);
        for (int i = 1; i < nums.length - 1; i++) {
            Integer c = t.ceiling(nums[i]);
            if (c != null) {
                t.remove(c);
            }
            t.add(nums[i]);
            dp1[i] = t.size();
        }

        int[] dp2 = new int[nums.length];
        t.clear();
        t.add(nums[nums.length - 1]);
        for (int i = nums.length - 2; i > 0; i--) {
            Integer c = t.ceiling(nums[i]);
            if (c != null) {
                t.remove(c);
            }
            t.add(nums[i]);
            dp2[i] = t.size();
            if (dp1[i] > 1 && dp2[i] > 1) {
                res = Math.max(res, dp1[i] + dp2[i] - 1);
            }
        }
        return nums.length - res;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
//        TreeSet<Integer> t = new TreeSet<>();
//        t.add(1);
//        t.add(3);
//        t.add(5);
//        t.add(7);
//        System.out.println(t.ceiling(8));
        System.out.println(s.minimumMountainRemovals(new int[]{2, 1, 1, 5, 6, 2, 3, 1}));
    }
}
