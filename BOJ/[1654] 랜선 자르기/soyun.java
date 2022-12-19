/*
 * 풀이
 * https://whimsical-report-4b5.notion.site/1654-9593784614c14409818a0aed2f4ed221
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());

        int K = Integer.parseInt(stringTokenizer.nextToken());
        int N = Integer.parseInt(stringTokenizer.nextToken());

        int[] cable = new int[K];

        for(int i=0; i<K; i++) {
            cable[i] = Integer.parseInt(bufferedReader.readLine());
        }

        Arrays.sort(cable);

        long min = 1;
        long max = cable[K-1];

        while(min <= max) {
            long mid = (min + max) / 2;

            long count = 0;

            for(int i=0; i<K; i++) {
                count += cable[i] / mid;
            }

            if(count < N) {
                max = mid - 1;
            } else {
                min = mid + 1;
            }
        }

        System.out.println(max);
    }
}