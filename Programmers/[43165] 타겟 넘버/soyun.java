/*
 * 풀이
 * https://whimsical-report-4b5.notion.site/43165-315ea14c2e2e4e84bcafbddc2da4de55
 */

public class Main {
    static int answer = 0;

    public int solution(int[] numbers, int target) {
        dfs(numbers, target, 0, 0);

        return answer;
    }

    static void dfs(int[] numbers, int target, int index, int sum) {
        if(index == numbers.length) {
            if(sum == target) {
                answer++;
            }

            return;
        }

        dfs(numbers, target, index + 1, sum + numbers[index]);
        dfs(numbers, target, index + 1, sum - numbers[index]);
    }

    public static void main(String[] args) {
        int result = new Main().solution(new int[]{1, 1, 1, 1, 1}, 3);

        System.out.println("result: " + result);
    }
}
