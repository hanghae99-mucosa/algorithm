import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Seungchan {
    static int N;
    static int M;
    static int[] req;
    static int limit;
    static int trash = 0;
    static int sum = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        req = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i<N; i++){
            req[i] = Integer.parseInt(st.nextToken());
            sum+=req[i];
        }
        M = Integer.parseInt(br.readLine());

        Arrays.sort(req);

        if (sum <= M){
            System.out.println(req[N-1]);
        } else{
            int count = 0;
            OutLoop :
            for (int i = N-1; i > 0 ; i--) {
                if ((sum-trash)<M){
                    while(true){
                        trash -= count;
                        limit++;
                        if ((sum-trash)>M){
                            limit--;
                            trash += count;
                            break OutLoop;
                        }
                    }
                }
                count++;
                trash += count*(req[i]-req[i-1]);
                limit = req[i-1];
            }

            count++;
            while ((sum-trash)>M){
                limit--;
                trash += count;
            }
            
            System.out.println(limit);
        }
    }

}