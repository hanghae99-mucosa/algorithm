/*
 * 풀이
 * https://whimsical-report-4b5.notion.site/11726-2xn-7de5d506f6914873bc67c9c3a940ff3b
 */

import java.util.Scanner;

public class Main {
    static int n;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        n = scanner.nextInt();

        int[] answer = new int[1001];
        answer[1] = 1;
        answer[2] = 2;

        for(int i=3; i<n+1; i++) {
            answer[i] = (answer[i-1] + answer[i-2]) % 10007;
        }

        System.out.println(answer[n]);
    }
}
