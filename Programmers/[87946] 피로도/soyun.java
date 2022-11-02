/*
 * 풀이
 * https://whimsical-report-4b5.notion.site/87946-a7c20b9b0edb440bbf659f7dc24dbdf1
 */

public class Main {
    static boolean[] visited;
    static int answer = 0;

    public int solution(int k, int[][] dungeons) {
        visited = new boolean[dungeons.length];

        dfs(k, dungeons, 0);

        return answer;
    }

    public void dfs(int currentK, int[][] dungeons, int count) {
        for(int i=0; i<dungeons.length; i++) {
            if(!visited[i]) {
                if(dungeons[i][0] <= currentK) {
                    visited[i] = true;

                    dfs(currentK-dungeons[i][1], dungeons, count+1);

                    visited[i] = false;
                }
            }
        }

        if(count > answer) {
            answer = count;
        }
    }

    public static void main(String[] args) {
        int result = new Main().solution(80, new int[][]{{80,20},{50,40},{30,10}});

        System.out.println("result: " + result);
    }
}
