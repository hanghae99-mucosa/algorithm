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

//public class Main {
//    static int n;
//
//    public static void main(String[] args) {
//	    Scanner scanner = new Scanner(System.in);
//
//	    n = scanner.nextInt();
//
//	    int answer = 0;
//
//	    for(int i=0; i<n/2+1; i++) {
//	        answer += calculate(i);
//        }
//
//        System.out.println(answer);
//    }
//
//    static int calculate(int count) {
//        if(count == 0) {
//            return 1;
//        }
//
//        int temp = n - count;
//        int result = 1;
//
//        for(int i=0; i<count; i++) {
//            result = (result * temp) % 10007;
//
//            temp--;
//        }
//
//        for(int i=count; i>0; i--) {
//            result /= i;
//        }
//
//        return result;
//    }
//}
