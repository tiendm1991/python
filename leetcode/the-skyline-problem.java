package com.fss.tool.ReadAdapterObject.util;

import java.lang.reflect.Array;
import java.util.*;
import java.util.logging.Level;
import java.util.stream.Collectors;

class Solution {
    public List<List<Integer>> getSkyline(int[][] a) {
        List<int[]> points = new ArrayList<>();
        for (int[] b : a) {
            points.add(new int[]{b[0], -b[2]});
            points.add(new int[]{b[1], b[2]});
        }
        points.sort((p1, p2) -> {
            if (p1[0] != p2[0]) {
                return p1[0] - p2[0];
            }
            return p1[1] - p2[1];
        });
        int maxHeight = 0;
        TreeSet<int[]> t = new TreeSet<>((o1, o2) -> {
            if (o1[0] != o2[0]) {
                return o1[0] - o2[0];
            }
            return o1[1] - o2[1];
        });
        HashMap<Integer, Integer> count = new HashMap<>();
        List<List<Integer>> res = new ArrayList<>();
        for (int[] p : points) {
            if (p[1] < 0) {
                int c = 0;
                if (count.containsKey(-p[1])) {
                    c = count.get(-p[1]);
                }
                t.add(new int[]{-p[1], c + 1});
                count.put(-p[1], c + 1);
            } else {
                t.remove(t.ceiling(new int[]{p[1], 0}));
            }
            int curHeight = 0;
            if (!t.isEmpty()) {
                curHeight = t.last()[0];
            }
            if (maxHeight != curHeight) {
                res.add(Arrays.asList(p[0], curHeight));
                maxHeight = curHeight;
            }
        }
        return res;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
//        TreeSet<int[]> t = new TreeSet<>((o1, o2) -> {
//            if (o1[0] != o2[0]) {
//                return o1[0] - o2[0];
//            }
//            return o1[1] - o2[1];
//        });
//        t.add(new int[]{1, 1});
//        t.add(new int[]{1, 2});
//        t.add(new int[]{3, 1});
//        t.add(new int[]{4, 1});
//        t.add(new int[]{4, 2});
//        t.add(new int[]{4, 4});
//        t.add(new int[]{5, 1});
//        System.out.println(t.ceiling(new int[]{4, 1}));
//        System.out.println(t.remove(t.ceiling(new int[]{4, 0})));
//        System.out.println(t.remove(t.ceiling(new int[]{4, 0})));
//        System.out.println(t.ceiling(new int[]{4, 2}));
        System.out.println(s.getSkyline(new int[][]{
                new int[]{2, 9, 10},
                new int[]{3, 7, 15},
                new int[]{5, 12, 12},
                new int[]{15, 20, 10},
                new int[]{19, 24, 8}}));
    }
}
