/*
 * 풀이
 * https://whimsical-report-4b5.notion.site/10815-813b7859f2b54621be195a1276987ac2
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int[] NArray;

    public static void main(String[] args) throws IOException {
        // 주어진 값 입력받기
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(bufferedReader.readLine());
        NArray = new int[N];

        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());

        for(int i=0; i<N; i++) {
            NArray[i] = Integer.parseInt(stringTokenizer.nextToken());
        }

        int M = Integer.parseInt(bufferedReader.readLine());
        int[] MArray = new int[M];

        stringTokenizer = new StringTokenizer(bufferedReader.readLine());

        for(int i=0; i<M; i++) {
            MArray[i] = Integer.parseInt(stringTokenizer.nextToken());
        }

        // 상근이가 가지고 있는 숫자 카드 배열 정렬
        Arrays.sort(NArray);

        StringBuilder answer = new StringBuilder();

        for(int i=0; i<M; i++) {
            answer.append(searchCard(MArray[i])).append(" ");
        }

        System.out.println(answer);
    }

    static int searchCard(int number) {
        int firstIndex = 0;
        int lastIndex = N - 1;
        int middleIndex;

        while(firstIndex <= lastIndex) {
            middleIndex = (firstIndex + lastIndex) / 2;

            if(NArray[middleIndex] > number) {
                lastIndex = middleIndex - 1;
            } else if(NArray[middleIndex] == number) {
                return 1;
            } else {
                firstIndex = middleIndex + 1;
            }
        }

        return 0;
    }
}
