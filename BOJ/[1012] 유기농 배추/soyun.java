/*
 * 풀이
 * https://whimsical-report-4b5.notion.site/1012-a6437d67a0fd4c34810ee45ec2d9938f
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N, M, K;
    static int[][] Field;

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(bufferedReader.readLine());

        int answer = 0;

        for(int i=0; i<T; i++) {
            StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
            M = Integer.parseInt(stringTokenizer.nextToken());
            N = Integer.parseInt(stringTokenizer.nextToken());
            K = Integer.parseInt(stringTokenizer.nextToken());

            Field = new int[N][M];

            for(int j=0; j<K; j++) {
                stringTokenizer = new StringTokenizer(bufferedReader.readLine());
                int x = Integer.parseInt(stringTokenizer.nextToken());
                int y = Integer.parseInt(stringTokenizer.nextToken());

                Field[y][x] = 1;
            }

            answer = countEarthworm();

            System.out.println(answer);
        }
    }

    static int countEarthworm() {
        int earthworm = 0;

        for(int i=0; i<N; i++) {
            for(int j=0; j<M; j++) {
                if(Field[i][j] == 1) {
                    dfs(i, j);

                    earthworm++;
                }
            }
        }

        return earthworm;
    }

    static void dfs(int currentX, int currentY) {
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};

        for(int i=0; i<4; i++) {
            int nextX = currentX + dx[i];
            int nextY = currentY + dy[i];

            if(nextX>=0 && nextY>=0 && nextX<N && nextY<M) {
                if(Field[nextX][nextY] == 1) {
                    Field[nextX][nextY] = 2;

                    dfs(nextX, nextY);
                }
            }
        }
    }
}
