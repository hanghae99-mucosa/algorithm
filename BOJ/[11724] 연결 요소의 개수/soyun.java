/*
 * 풀이
 * https://whimsical-report-4b5.notion.site/11724-c6369da661b84ba4ba5e9a55ecbf5687
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());

        int N = Integer.parseInt(stringTokenizer.nextToken());
        int M = Integer.parseInt(stringTokenizer.nextToken());

        for(int i=0; i<=N; i++) {
            graph.add(new ArrayList<>());
        }

        for(int i=0; i<M; i++) {
            stringTokenizer = new StringTokenizer(bufferedReader.readLine());

            int u = Integer.parseInt(stringTokenizer.nextToken());
            int v = Integer.parseInt(stringTokenizer.nextToken());

            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        visited = new boolean[N+1];
        int answer = 0;

        for(int i=1; i<=N; i++) {
            if(!visited[i]) {
                dfs(i);

                answer++;
            }
        }

        System.out.println(answer);
    }

    static void dfs(int n) {
        visited[n] = true;

        ArrayList<Integer> nextList = graph.get(n);

        for(int next : nextList) {
            if(!visited[next]) {
                dfs(next);
            }
        }
    }
}