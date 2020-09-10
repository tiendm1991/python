package leetcode;

import java.util.Arrays;
import java.util.PriorityQueue;

public class Solution {
	public int scheduleCourse(int[][] courses) {
		Arrays.sort(courses, (c1, c2) -> c1[1] - c2[1]);
		PriorityQueue<Integer> max_heap = new PriorityQueue<Integer>((x, y) -> y - x);
		int s = 0;
		for (int[] c: courses) {
			s += c[0];
			max_heap.add(c[0]);
			if (s > c[1]) {
				s -= max_heap.poll();
			}
		}
		return max_heap.size();
	}

	public static void main(String[] args) {
		int[][] courses = new int[][] { 
			{ 9, 10 }, 
			{ 3, 12 }, 
			{ 7, 17 }, 
			{ 4, 18 },
			{ 10, 19 }, 
			{ 10, 20 }, 
			{ 5, 20 }, 
		};
		Solution s = new Solution();
		System.out.println(s.scheduleCourse(courses));
	}
}
