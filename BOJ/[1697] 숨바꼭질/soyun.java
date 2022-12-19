/*
 * 풀이
 * https://whimsical-report-4b5.notion.site/1697-8cd3185fe1f146e9a559110532174006
 */

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    static final int MAX = 100_001;
    static int N, K;

    public static void main(String[] args) {
	    Scanner scanner = new Scanner(System.in);
	    N = scanner.nextInt();
	    K = scanner.nextInt();

	    int answer;

	    if(N == K) {
            answer = 0;
        } else if(N > K) {
            answer = N - K;
        } else {
            answer = bfs();
        }

        System.out.println(answer);
    }

    static int bfs() {
        boolean[] visited = new boolean[MAX];
        int[] seconds = new int[MAX];

        Queue<Integer> queue = new LinkedList<>();
        visited[N] = true;
        queue.add(N);

        while(!queue.isEmpty()) {
            int current = queue.remove();

            int[] nextArray = {current-1, current+1, current*2};

            for(int next : nextArray) {
                if(next<0 || next>=MAX) {
                    continue;
                }

                if(visited[next]) {
                    continue;
                }

                visited[next] = true;
                seconds[next] = seconds[current] + 1;

                if(next == K) {
                    break;
                }

                queue.add(next);
            }
        }

        return seconds[K];
    }
}
