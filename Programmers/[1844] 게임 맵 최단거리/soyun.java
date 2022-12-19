/*
 * 풀이
 * https://whimsical-report-4b5.notion.site/1844-38eead7ed5924bf195b245ba927ec992
 */

import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public int solution(int[][] maps) {
        int N = maps[0].length; // 가로
        int M = maps.length; // 세로

        int[][] visited = new int[M][N];
        Queue<int[]> queue = new LinkedList<>();

        visited[0][0] = 1;
        queue.add(new int[]{0, 0});

        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};

        while(!queue.isEmpty()) {
            int[] current = queue.remove();
            int currentX = current[0];
            int currentY = current[1];

            if(currentX==N-1 && currentY==M-1) {
                break;
            }

            for(int i=0; i<4; i++) {
                int nextX = currentX + dx[i];
                int nextY = currentY + dy[i];

                if(nextX>=0 && nextY>=0 && nextX<N && nextY<M) {
                    if(visited[nextY][nextX]==0 && maps[nextY][nextX]!=0) {
                        visited[nextY][nextX] = visited[currentY][currentX] + 1;

                        queue.add(new int[]{nextX, nextY});
                    }
                }
            }
        }

        return visited[M-1][N-1]!=0 ? visited[M-1][N-1] : -1;
    }

    public static void main(String[] args) {
        int result = new Main().solution(new int[][]{{1,0,1,1,1},{1,0,1,0,1},{1,0,1,1,1},{1,1,1,0,1},{0,0,0,0,1}});

        System.out.println("result: " + result);
    }
}