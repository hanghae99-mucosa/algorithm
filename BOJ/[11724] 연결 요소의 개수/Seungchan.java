import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Stack;
import java.util.StringTokenizer;

public class Seungchan {
    static int N;
    static int M;
    static ArrayList<Integer>[] adj;
    static boolean visited[];
    static  int count = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        adj = new ArrayList[N];
        visited = new boolean[N];

        for(int i=0; i<N; i++){
            adj[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++){
            st = new StringTokenizer(br.readLine());
            int v1 = Integer.parseInt(st.nextToken())-1;
            int v2 = Integer.parseInt(st.nextToken())-1;

            adj[v1].add(v2);
            adj[v2].add(v1);
        }

        for (int v = 0; v < N; v++){
            if (!visited[v]){
                dfs(v);
                count ++;
            }
        }

        System.out.println(count);
    }

    static void dfs(int v){
        Stack<Integer> stack = new Stack<Integer>();

        stack.push(v);
        visited[v] = true;

        while (!stack.isEmpty()){
            int  nextV = stack.pop();

            for (int linkedV : adj[nextV]) {
                if(!visited[linkedV]) {
                    stack.push(linkedV);
                    visited[linkedV] = true;
                }
            }
        }
    }
}