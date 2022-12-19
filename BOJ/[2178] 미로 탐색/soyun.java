/*
 * 풀이
 * https://whimsical-report-4b5.notion.site/2178-e761439ad53e443bbd8cd7268c2376b6
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int N, M;

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        N = Integer.parseInt(stringTokenizer.nextToken());
        M = Integer.parseInt(stringTokenizer.nextToken());

        int[][] maze = new int[N][M];

        for(int i=0; i<N; i++) {
            String temp = bufferedReader.readLine();

            for(int j=0; j<M; j++) {
                maze[i][j] = temp.charAt(j) - '0';
            }
        }

        int answer = bfs(maze);

        System.out.println(answer);
    }

    static int bfs(int[][] maze) {
        boolean[][] visited = new boolean[N][M];
        int[][] step = new int[N][M];

        Queue<int[]> queue = new LinkedList<>();
        visited[0][0] = true;
        step[0][0] = 1;
        queue.add(new int[] {0,0});

        while(!queue.isEmpty()) {
            int[] current = queue.remove();
            int currentX = current[0];
            int currentY = current[1];

            int[] dx = {-1, 1, 0, 0};
            int[] dy = {0, 0, -1, 1};

            for(int i=0; i<4; i++) {
                int nextX = currentX + dx[i];
                int nextY = currentY + dy[i];

                if(nextX<0 || nextY<0 || nextX>=N || nextY>=M) {
                    continue;
                }

                if(maze[nextX][nextY] == 0) {
                    continue;
                }

                if(visited[nextX][nextY]) {
                    continue;
                }

                visited[nextX][nextY] = true;
                step[nextX][nextY] = step[currentX][currentY] + 1;

                if(nextX == N-1 && nextY == M-1) {
                    break;
                }

                queue.add(new int[] {nextX, nextY});
            }
        }

        return step[N-1][M-1];
    }
}