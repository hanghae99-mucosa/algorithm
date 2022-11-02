/*
 * 풀이
 * https://whimsical-report-4b5.notion.site/10026-7726f04d189149e08786b2492d5cdd9a
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    static int N;
    static char[][] nPainting;
    static char[][] cbPainting;
    static boolean[][] visited;

    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(bufferedReader.readLine());

        nPainting = new char[N][N];
        cbPainting = new char[N][N];

        for(int i=0; i<N; i++) {
            nPainting[i] = bufferedReader.readLine().toCharArray();

            for(int j=0; j<N; j++) {
                if(nPainting[i][j] == 'G') {
                    cbPainting[i][j] = 'R';
                } else {
                    cbPainting[i][j] = nPainting[i][j];
                }
            }
        }

        // 색약이 아닌 사람의 경우
        visited = new boolean[N][N];
        int nArea = 0;

        for(int i=0; i<N; i++) {
            for(int j=0; j<N; j++) {
                if(!visited[i][j]) {
                    bfs(nPainting, j, i);

                    nArea++;
                }
            }
        }

        // 색약인 사람의 경우
        visited = new boolean[N][N];
        int cbArea = 0;

        for(int i=0; i<N; i++) {
            for(int j=0; j<N; j++) {
                if(!visited[i][j]) {
                    bfs(cbPainting, j, i);

                    cbArea++;
                }
            }
        }

        System.out.println(nArea + " " + cbArea);
    }

    static void bfs(char[][] painting, int x, int y) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{x, y});

        while(!queue.isEmpty()) {
            int[] current = queue.remove();
            int currentX = current[0];
            int currentY = current[1];

            for(int i=0; i<4; i++) {
                int nextX = currentX + dx[i];
                int nextY = currentY + dy[i];

                if(nextX>=0 && nextY>=0 && nextX<N && nextY<N) {
                    if(painting[nextY][nextX] == painting[currentY][currentX] && !visited[nextY][nextX]) {
                        visited[nextY][nextX] = true;

                        queue.add(new int[]{nextX, nextY});
                    }
                }
            }
        }
    }
}