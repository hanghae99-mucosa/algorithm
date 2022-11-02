/*
 * 풀이
 * https://whimsical-report-4b5.notion.site/12985-aa2b9ad251cb466ba878cde4dea1d8de
 */

public class Main {
    public int solution(int n, int a, int b) {
        int answer = 1;

        int aCount = a;
        int bCount = b;

        while(true) {
            aCount = (int) Math.ceil(aCount / 2.0);
            bCount = (int) Math.ceil(bCount / 2.0);

            if(aCount == bCount) {
                return answer;
            }

            answer++;
        }
    }

    public static void main(String[] args) {
        int result = new Main().solution(8, 4, 7);

        System.out.println("result: " + result);
    }
}
