/*
 * 풀이
 * https://whimsical-report-4b5.notion.site/7562-e93b8189fae74739b3c720d21e9e03d3
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    static int I;
    static int[] start = new int[2];
    static int[] end = new int[2];
    static int[][] visited;

    static int[] dx = {-1, 1, -2, 2, -1, 1, -2, 2};
    static int[] dy = {-2, -2, -1, -1, 2, 2, 1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader  bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(bufferedReader.readLine());

        int[] result = new int[N];

        for(int i=0; i<N; i++) {
            I = Integer.parseInt(bufferedReader.readLine());

            String temp = bufferedReader.readLine();
            start[0] = Integer.parseInt(temp.split(" ")[0]);
            start[1] = Integer.parseInt(temp.split(" ")[1]);

            temp = bufferedReader.readLine();
            end[0] = Integer.parseInt(temp.split(" ")[0]);
            end[1] = Integer.parseInt(temp.split(" ")[1]);

            if(start[0]==end[0] && start[1]==end[1]) {
                result[i] = 0;
            } else {
                bfs();

                result[i] = visited[end[1]][end[0]];
            }

            System.out.println(result[i]);
        }
    }

    static void bfs() {
        visited = new int[I][I];

        for(int i=0; i<I; i++) {
            for(int j=0; j<I; j++) {
                visited[i][j] = -1;
            }
        }

        Queue<int[]> queue = new LinkedList<>();

        visited[start[1]][start[0]] = 0;
        queue.add(new int[]{start[0], start[1]});

        while(!queue.isEmpty()) {
            int[] current = queue.remove();
            int currentX = current[0];
            int currentY = current[1];

            if(currentX==end[0] && currentY==end[1]) {
                break;
            }

            for(int i=0; i<8; i++) {
                int nextX = currentX + dx[i];
                int nextY = currentY + dy[i];

                if(nextX>=0 && nextY>=0 && nextX<I && nextY<I) {
                    if(visited[nextY][nextX] == -1) {
                        visited[nextY][nextX] = visited[currentY][currentX] + 1;

                        queue.add(new int[]{nextX, nextY});
                    }
                }
            }
        }
    }
}
