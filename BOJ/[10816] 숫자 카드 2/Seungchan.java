import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Seungchan {
    static int N;
    static int M;
    static HashMap<Integer,Integer> cards = new HashMap<>();
    static StringBuilder result = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int card;

        for (int i = 0; i < N; i++){
            card = Integer.parseInt(st.nextToken());
            cards.put(card, cards.getOrDefault(card, 0)+1);
        }

        st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++){
            card = Integer.parseInt(st.nextToken());
            result.append(cards.getOrDefault(card,0)+" ");
        }

        System.out.println(result.toString());
    }
}
