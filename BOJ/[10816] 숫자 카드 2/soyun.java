/*
 * 풀이
 * https://whimsical-report-4b5.notion.site/10816-2-1744c51764a64b7991c4c7bcc03362dd
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
    static HashMap<Integer, Integer> cards = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(bufferedReader.readLine());

        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());

        for(int i=0; i<N; i++) {
            int temp = Integer.parseInt(stringTokenizer.nextToken());

            if(cards.containsKey(temp)) {
                cards.put(temp, cards.get(temp) + 1);
            } else {
                cards.put(temp, 1);
            }
        }

        int M = Integer.parseInt(bufferedReader.readLine());

        stringTokenizer = new StringTokenizer(bufferedReader.readLine());

        StringBuilder stringBuilder = new StringBuilder();

        for(int i=0; i<M; i++) {
            int current = Integer.parseInt(stringTokenizer.nextToken());

            if(!cards.containsKey(current)) {
                stringBuilder.append(0);
            } else {
                stringBuilder.append(cards.get(current));
            }

            if(i != M-1) {
                stringBuilder.append(" ");
            }
        }

        System.out.println(stringBuilder.toString());
    }
}
