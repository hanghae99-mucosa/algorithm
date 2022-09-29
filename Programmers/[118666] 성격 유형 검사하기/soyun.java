/*
 * 풀이
 * https://whimsical-report-4b5.notion.site/118666-fce3e000515d45ab8762cbbf9c91ace5
 */

import java.util.HashMap;

public class Main {
    public String solution(String[] survey, int[] choices) {
        int[] score = {0, 3, 2, 1, 0, 1, 2, 3};

        HashMap<Character, Integer> scoreMap = new HashMap<>();
        scoreMap.put('R', 0);
        scoreMap.put('T', 0);
        scoreMap.put('C', 0);
        scoreMap.put('F', 0);
        scoreMap.put('J', 0);
        scoreMap.put('M', 0);
        scoreMap.put('A', 0);
        scoreMap.put('N', 0);

        for(int i=0; i<survey.length; i++) {
            char disagree = survey[i].charAt(0);
            char agree = survey[i].charAt(1);

            if(choices[i] < 4) {
                scoreMap.put(disagree, scoreMap.get(disagree) + score[choices[i]]);
            } else if(choices[i] > 4) {
                scoreMap.put(agree, scoreMap.get(agree) + score[choices[i]]);
            }
        }

        StringBuilder result = new StringBuilder();

        if(scoreMap.get('R') >= scoreMap.get('T')) {
            result.append("R");
        } else {
            result.append("T");
        }

        if(scoreMap.get('C') >= scoreMap.get('F')) {
            result.append("C");
        } else {
            result.append("F");
        }

        if(scoreMap.get('J') >= scoreMap.get('M')) {
            result.append("J");
        } else {
            result.append("M");
        }

        if(scoreMap.get('A') >= scoreMap.get('N')) {
            result.append("A");
        } else {
            result.append("N");
        }

        return result.toString();
    }

    public static void main(String[] args) {
        String result = new Main().solution(new String[]{"AN", "CF", "MJ", "RT", "NA"}, new int[]{5, 3, 2, 7, 5});

        System.out.println("result: " + result);
    }
}
