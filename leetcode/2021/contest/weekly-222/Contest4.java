import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;

class Solution {
    public int minOperations(int[] target, int[] arr) {
        Map<Integer, Integer> indices = new HashMap<>();
        for (int i = 0; i < target.length; i++) {
            indices.put(target[i], i);
        }
        for (int i = 0; i < arr.length; i++) {
            if (indices.containsKey(arr[i])) {
                arr[i] = indices.get(arr[i]);
            } else {
                arr[i] = Integer.MAX_VALUE;
            }
        }
        TreeSet<Integer> set = new TreeSet<>();
        for (int x : arr) {
            Integer y = set.ceiling(x);
            if (y != null) {
                set.remove(y);
            }
            set.add(x);
        }
        if (set.last() == Integer.MAX_VALUE) {
            set.pollLast();
        }
        return target.length - set.size();
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] target = new int[]{6, 4, 8, 1, 3, 2};
        int[] arr = new int[]{4, 7, 6, 2, 3, 8, 6, 1};
        System.out.println(s.minOperations(target, arr));
    }
}