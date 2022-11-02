/*
 * 풀이
 * https://whimsical-report-4b5.notion.site/2468-43eb5622c07c4ac499c22c0ba0cd9961
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int[][] map;
    static int minHeight = 0;
    static int maxHeight = 0;
    static int[][] sink;
    static boolean[][] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(bufferedReader.readLine());

        map = new int[N][N];

        for(int i=0; i<N; i++) {
            StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());

            for(int j=0; j<N; j++) {
                map[i][j] = Integer.parseInt(stringTokenizer.nextToken());

                if(minHeight == 0) minHeight = map[i][j];
                else if(maxHeight == 0) maxHeight = map[i][j];
                else {
                    if(map[i][j] < minHeight) minHeight = map[i][j];
                    else if(map[i][j] > maxHeight) maxHeight = map[i][j];
                }
            }
        }

        int max = 1; // 최소 안전지대 수 : 1

        sink = new int[N][N];
        int rain = minHeight;

        while(rain < maxHeight) {
            // 잠긴 지역 구하기
            for(int i=0; i<N; i++) {
                for(int j=0; j<N; j++) {
                    if(sink[i][j] == 1) {
                        continue;
                    }

                    if(map[i][j] <= rain) {
                        sink[i][j] = 1;
                    }
                }
            }

            visited = new boolean[N][N];
            int safeArea = 0;

            // 탐색 시작점 구하기
            for(int i=0; i<N; i++) {
                for(int j=0; j<N; j++) {
                    if(sink[i][j]==0 && !visited[i][j]) {
                        bfs(j, i);

                        safeArea++;
                    }
                }
            }

            if(safeArea > max) {
                max = safeArea;
            }

            rain++;
        }

        System.out.println(max);
    }

    static void bfs(int x, int y) {
        Queue<int[]> queue = new LinkedList<>();
        visited[y][x] = true;
        queue.add(new int[]{y, x});

        int[] dy = {-1, 1, 0, 0};
        int[] dx = {0, 0, -1, 1};

        while(!queue.isEmpty()) {
            int[] current = queue.remove();
            int currentY = current[0];
            int currentX = current[1];

            for(int i=0; i<4; i++) {
                int nextY = currentY + dy[i];
                int nextX = currentX + dx[i];

                if(nextX>=0 && nextY>=0 && nextX<N && nextY<N) {
                    if(sink[nextY][nextX]==0 && !visited[nextY][nextX]) {
                        visited[nextY][nextX] = true;

                        queue.add(new int[]{nextY, nextX});
                    }
                }
            }
        }
    }
}
