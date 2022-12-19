/*
 * 풀이
 * https://whimsical-report-4b5.notion.site/42842-22afe22795bd4b659721a9298c07fe92
 */

import java.util.ArrayList;
import java.util.Arrays;

public class Main {
    public int[] solution(int brown, int yellow) {
        ArrayList<int[]> yellowDivisor = new ArrayList<>();

        if(yellow == 1) {
            yellowDivisor.add(new int[]{1, 1});
        } else {
            for(int i=1; i<=Math.sqrt(yellow); i++) {
                if(yellow % i == 0) {
                    yellowDivisor.add(new int[]{yellow/i, i});
                }
            }
        }

        int[] answer = new int[1];

        for(int i=0; i<yellowDivisor.size(); i++) {
            int width = yellowDivisor.get(i)[0];
            int height = yellowDivisor.get(i)[1];

            if((width+2)*2 + height*2 == brown) {
                answer = new int[]{width + 2, height + 2};

                break;
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        int[] result = new Main().solution(10, 2);

        System.out.println("result: " + Arrays.toString(result));
    }
}
