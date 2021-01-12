import java.util.HashMap;
import java.util.Map;
import java.util.TreeSet;

public class Solution {
    public int oddEvenJumps(int[] a) {
        int n = a.length;
        TreeSet<Integer> set = new TreeSet();
        Map<Integer, Integer> map = new HashMap<>();
        boolean[] oddDp = new boolean[n];
        boolean[] evenDp = new boolean[n];
        oddDp[n - 1] = true;
        evenDp[n - 1] = true;
        set.add(a[n - 1]);
        map.put(a[n - 1], n - 1);
        int res = 1;
        for (int i = n - 2; i >= 0; i--) {
            Integer ceil = set.ceiling(a[i]);
            Integer floor = set.floor(a[i]);
            if (ceil != null && evenDp[map.get(ceil)]) {
                res++;
                oddDp[i] = true;
            }
            if (floor != null && oddDp[map.get(floor)]) {
                evenDp[i] = true;
            }
            set.add(a[i]);
            map.put(a[i], i);
        }
        return res;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.oddEvenJumps(new int[]{10, 13, 12, 14, 15}));
        System.out.println(s.oddEvenJumps(new int[]{2, 3, 1, 1, 4}));
        System.out.println(s.oddEvenJumps(new int[]{5, 1, 3, 4, 2}));
    }
}
