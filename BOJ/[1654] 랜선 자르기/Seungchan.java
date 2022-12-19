import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Seungchan {
    static int K;
    static int N;
    static int[] lan;
    static int count;

    static long low = 1;
    static long high = -1;
    static long mid;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        K = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        lan = new int[K];
        for (int i = 0; i<K; i++){
            lan[i] = Integer.parseInt(br.readLine());
            if (high < lan[i]) high = lan[i];
        }

        while(low<=high){
            count = 0;
            mid = (high+low)/2;

            for (int i = 0; i < K; i++) {
                count += lan[i]/mid;
            }

            if(count<N){
                high = mid-1;
            } else{
                low = mid+1;
            }
        }

        System.out.println(high);
        
        // for (int i = 0; i < K; i++){
        //     count += lan[i]/low;
        // }

        // if (count<N){
        //     System.out.println(high);
        // }else {
        //     System.out.println(low);
        // }
    }

}