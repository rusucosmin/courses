import java.util.Scanner;

public class Edrandr {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int T = in.nextInt();
        /*
        Student should not have fail any of the exams.
        Student must obtain a full score in some of his/her exams to show that he/she is excellent in some of the subjects.
        He/She must have a grade point average not less than 4.0
        */
        for(int t = 0; t < T; ++ t) {
            int n = in.nextInt();
            boolean failed = false;
            boolean maximum = false;
            int sum = 0;
            for(int i = 0; i < n; ++ i) {
                int now = in.nextInt();
                if(now == 2)
                    failed = true;
                if(now == 5)
                    maximum = true;
                sum += now;
            }
            if(!failed && maximum && sum >= 4 * n)
                System.out.println("Yes");
            else
                System.out.println("No");
        }
    }
}
