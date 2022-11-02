/*
 * 풀이
 * https://whimsical-report-4b5.notion.site/60058-9b8641516fae4d90bd81fc2a44e28f77
 */

public class Main {
    static StringBuilder u;
    static StringBuilder v;
    static StringBuilder temp = new StringBuilder();

    public String solution(String p) {
        String answer = convert(p);

        return answer;
    }

    void split(String s) {
        int check = 0;

        u = new StringBuilder();
        v = new StringBuilder();

        for(int i=0; i<s.length(); i++) {
            if(s.charAt(i) == '(') {
                u.append(s.charAt(i));

                check++;
            } else if(s.charAt(i) == ')') {
                u.append(s.charAt(i));

                check--;
            }

            if(check == 0) {
                v.append(s.substring(i+1));

                break;
            }
        }
    }

    boolean check(String s) {
        int check = 0;

        for(int i=0; i<s.length(); i++) {
            if(s.charAt(i) == '(') {
                check++;
            } else if(s.charAt(i) == ')') {
                check--;
            }

            if(check < 0) {
                return false;
            }
        }

        return true;
    }

    String convert(String s) {
        if(s.isBlank()) {
            return "";
        }

        split(s);

        if(check(u.toString())) {
            temp.append(u.toString());

            convert(v.toString());
        } else {
            String uString = u.toString();

            temp.append("(");

            convert(v.toString());

            temp.append(")");

            uString = uString.substring(1, uString.length()-1);

            for(int i=0; i<uString.length(); i++) {
                if(uString.charAt(i) == '(') {
                    temp.append(")");
                } else if(uString.charAt(i) == ')') {
                    temp.append("(");
                }
            }

            temp.append(v.toString());
        }

        return temp.toString();
    }

    public static void main(String[] args) {
        String result = new Main().solution("()))((()");

        System.out.println("result: " + result);
    }
}
