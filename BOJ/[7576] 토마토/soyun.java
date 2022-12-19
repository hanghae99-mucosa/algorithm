/*
 * 풀이
 * https://whimsical-report-4b5.notion.site/7576-6a1034a76acd4879b5791954483e8daa
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
        M = Integer.parseInt(stringTokenizer.nextToken());
        N = Integer.parseInt(stringTokenizer.nextToken());

        int[][] box = new int[N][M];

        for(int i=0; i<N; i++) {
            stringTokenizer = new StringTokenizer(bufferedReader.readLine());

            for(int j=0; j<M; j++) {
                box[i][j] = Integer.parseInt(stringTokenizer.nextToken());
            }
        }

        int answer = bfs(box);

        System.out.println(answer);
    }

    static int bfs(int[][] box) {
        int count = 0;
        int day = 0;

        Queue<int[]> currentQueue = new LinkedList<>();

        for(int i=0; i<N; i++) {
            for(int j=0; j<M; j++) {
                if(box[i][j] == 1) {
                    currentQueue.add(new int[] {i, j});
                } else if(box[i][j] == 0) {
                    count++;
                }
            }
        }

        while(!currentQueue.isEmpty()) {
            Queue<int[]> nextQueue = new LinkedList<>();

            while(!currentQueue.isEmpty()) {
                int[] current = currentQueue.remove();
                int currentX = current[0];
                int currentY = current[1];

                int[] dx = {-1, 1, 0, 0};
                int[] dy = {0, 0, -1, 1};

                for(int i=0; i<4; i++) {
                    int nextX = currentX + dx[i];
                    int nextY = currentY + dy[i];

                    if(nextX>=0 && nextY>=0 && nextX<N && nextY<M) {
                        if(box[nextX][nextY] == 0) {
                            box[nextX][nextY] = 1;

                            nextQueue.add(new int[] {nextX, nextY});
                            count--;
                        }
                    }
                }
            }

            if(!nextQueue.isEmpty()) {
                currentQueue.addAll(nextQueue);
                day++;
            }
        }

        return count==0 ? day : -1;
    }
}
