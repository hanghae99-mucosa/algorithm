/*
 * 풀이
 * https://whimsical-report-4b5.notion.site/68645-208353c36f1646a7a3896cd9570143cc
 */

import java.util.Arrays;

public class Main {
    public int[] solution(int n) {
        int[][] board = new int[n][n];
        int num = 1;
        int x = 0;
        int y = -1;

        for(int i=0; i<n; i++) {
            for(int j=i; j<n; j++) {
                if(i%3 == 0) {
                    y++;
                } else if(i%3 == 1) {
                    x++;
                } else {
                    x--;
                    y--;
                }

                board[y][x] = num;

                num++;
            }
        }

        int total = (n * (n + 1)) / 2;
        int[] answer = new int[total];
        int temp = 0;

        for(int i=0; i<n; i++) {
            for(int j=0; j<=i; j++) {
                answer[temp] = board[i][j];

                temp++;
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        int[] result = new Main().solution(4);

        System.out.println("result: " + Arrays.toString(result));
    }
}
