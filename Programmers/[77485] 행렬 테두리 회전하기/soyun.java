/*
 * 풀이
 * https://whimsical-report-4b5.notion.site/77485-8df2c2c30ad74265a3e17f7dcf37da82
 */

import java.util.Arrays;

public class Main {
    static int[][] matrix;

    public int[] solution(int rows, int columns, int[][] queries) {
        matrix = new int [rows][columns];

        int temp = 1;

        for(int i=0; i<rows; i++) {
            for(int j=0; j<columns; j++) {
                matrix[i][j] = temp;

                temp++;
            }
        }

        int[] answer = new int[queries.length];

        for(int i=0; i<queries.length; i++) {
            answer[i] = rotation(queries[i]);
        }

        return answer;
    }

    int rotation(int[] query) {
        int x1 = query[0] - 1;
        int y1 = query[1] - 1;
        int x2 = query[2] - 1;
        int y2 = query[3] - 1;

        int temp = matrix[x1][y1];
        int min = temp;

        for(int i=x1; i<x2; i++) {
            matrix[i][y1] = matrix[i+1][y1];

            if(matrix[i][y1] < min) {
                min = matrix[i][y1];
            }
        }

        for(int i=y1; i<y2; i++) {
            matrix[x2][i] = matrix[x2][i+1];

            if(matrix[x2][i] < min) {
                min = matrix[x2][i];
            }
        }

        for(int i=x2; i>x1; i--) {
            matrix[i][y2] = matrix[i-1][y2];

            if(matrix[i][y2] < min) {
                min = matrix[i][y2];
            }
        }

        for(int i=y2; i>y1; i--) {
            matrix[x1][i] = matrix[x1][i-1];

            if(matrix[x1][i] < min) {
                min = matrix[x1][i];
            }
        }

        matrix[x1][y1+1] = temp;

        return min;
    }

    public static void main(String[] args) {
        int[] result = new Main().solution(6, 6, new int[][]{{2,2,5,4},{3,3,6,6},{5,1,6,3}});

        System.out.println("result: " + Arrays.toString(result));
    }
}
