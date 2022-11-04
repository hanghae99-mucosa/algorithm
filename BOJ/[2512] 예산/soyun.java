/*
 * 풀이
 * https://whimsical-report-4b5.notion.site/2512-8fe6030114014b20975a3898bba0ddac
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(bufferedReader.readLine());

        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());

        int[] needs = new int[N];
        int needsSum = 0;

        for(int i=0; i<N; i++) {
            needs[i] = Integer.parseInt(stringTokenizer.nextToken());

            needsSum += needs[i];
        }

        int M = Integer.parseInt(bufferedReader.readLine());

        Arrays.sort(needs);

        int answer = 0;

        if(M >= needsSum) {
            answer = needs[N-1];
        } else {
            int expected = M / N;
            int sum = 0;

            while(sum <= M) {
                for(int i=0; i<N; i++) {
                    sum += Math.min(needs[i], expected);
                }

                if(sum <= M) {
                    expected++;

                    sum = 0;
                } else {
                    answer = expected - 1;

                    break;
                }
            }
        }

        System.out.println(answer);
    }
}
