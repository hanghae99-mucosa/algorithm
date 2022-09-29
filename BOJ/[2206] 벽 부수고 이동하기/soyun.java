/*
 * 풀이
 * https://whimsical-report-4b5.notion.site/2206-73c4b99eed3948aaafc934a4ae8bfd99
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

        int[][] map = new int[N+1][M+1];

        for(int i=1; i<N+1; i++) {
            String temp = bufferedReader.readLine();

            for(int j=1; j<M+1; j++) {
                map[i][j] = temp.charAt(j-1) - '0';
            }
        }

        int answer;

        if(N==1 && M==1) {
            answer = 1;
        } else {
            answer = bfs(map);
        }

        System.out.println(answer);
    }

    static int bfs(int[][] map) {
        int[][][] visited = new int[N+1][M+1][2];

        Queue<int[]> queue = new LinkedList<>();
        visited[1][1][0] = 1;
        queue.add(new int[] {1,1,0});

        while(!queue.isEmpty()) {
            int[] current = queue.remove();
            int currentX = current[0];
            int currentY = current[1];
            int currentWallFlag = current[2];

            int[] dx = {-1, 1, 0, 0};
            int[] dy = {0, 0, -1, 1};

            for(int i=0; i<4; i++) {
                int nextX = currentX + dx[i];
                int nextY = currentY + dy[i];
                int nextWallFlag = currentWallFlag;

                if(nextX<1 || nextY<1 || nextX>=N+1 || nextY>=M+1) {
                    continue;
                }

                if(visited[nextX][nextY][nextWallFlag] != 0) {
                    continue;
                }

                if(map[nextX][nextY] == 1) {
                    if(nextWallFlag == 0) {
                        visited[nextX][nextY][1] = visited[currentX][currentY][0] + 1;
                        nextWallFlag = 1;
                    } else {
                        continue;
                    }
                } else {
                    visited[nextX][nextY][nextWallFlag] = visited[currentX][currentY][currentWallFlag] + 1;
                }

                if(nextX==N && nextY==M) {
                    return visited[N][M][nextWallFlag];
                }

                queue.add(new int[] {nextX, nextY, nextWallFlag});
            }
        }

        return -1;
    }
}