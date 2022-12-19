/*
 * 풀이
 * https://whimsical-report-4b5.notion.site/77486-e4e655797ab941acbfa6299dac50bafe
 */

import java.util.Arrays;
import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedHashMap;

public class Main {
    static HashMap<String, String> parentMap = new HashMap<>();
    static LinkedHashMap<String, Integer> moneyMap = new LinkedHashMap<>();

    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {
        for(int i=0; i<enroll.length; i++) {
            parentMap.put(enroll[i], referral[i]);
            moneyMap.put(enroll[i], 0);
        }

        for(int i=0; i<seller.length; i++) {
            calculate(seller[i], amount[i]);
        }

        int[] answer = new int[enroll.length];
        Iterator<String> iterator = moneyMap.keySet().iterator();

        for(int i=0; i<enroll.length; i++) {
            String key = iterator.next();
            answer[i] = moneyMap.get(key);
        }

        return answer;
    }

    void calculate(String seller, int amount) {
        String now = seller;

        int totalProfit = 100 * amount;
        int parentProfit = 0;
        int childProfit;

        while(!now.equals("-")) {
            parentProfit = totalProfit / 10;
            childProfit = totalProfit - parentProfit;

            moneyMap.put(now, moneyMap.get(now) + childProfit);

            if(parentProfit < 1) {
                break;
            }

            now = parentMap.get(now);

            totalProfit = parentProfit;
        }
    }

    public static void main(String[] args) {
        int[] result = new Main().solution(new String[]{"john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"}, new String[]{"-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"}, new String[]{"young", "john", "tod", "emily", "mary"}, new int[]{12, 4, 2, 5, 10});

        System.out.println("result: " + Arrays.toString(result));
    }
}
