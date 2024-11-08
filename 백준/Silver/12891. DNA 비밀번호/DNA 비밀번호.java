import java.util.*;
import java.io.*;
public class Main {

    public static int change(char target) {
        if (target == 'A') {
            return 0;
        } else if (target == 'C') {
            return 1;
        } else if (target == 'G') {
            return 2;
        } else if (target == 'T') {
            return 3;
        }
        return -1;
    }

    public static void main(String [] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int dN = Integer.parseInt(st.nextToken());
        int sN = Integer.parseInt(st.nextToken());

        char [] dna = br.readLine().toCharArray();

        st = new StringTokenizer(br.readLine());
        int [] acgt= new int[4];
        for(int i=0; i<4; i++){
            acgt[i] = Integer.parseInt(st.nextToken());
        }

        int start = 0;
        int end = start + sN -1;
        int [] count = new int[4];

        for(int i=start; i<=end; i++){
            int index = change(dna[i]);
            if(index!=-1){
                count[index]+=1;
            }
        }

        int answer=0;
        while (end < dN){
            int check=0;
            for(int i=0; i<4; i++){
                if(acgt[i] <= count[i]){
                    check+=1;
                }
            }
            if(check==4) {
                answer += 1;
            }

            if(end==dN-1){
                break;
            }

            int s_index = change(dna[start]);
            if (s_index!=-1){
                count[s_index]-=1;
            }
            start+=1;
            end+=1;
            int e_index = change(dna[end]);
            if (e_index!=-1) {
                count[e_index] += 1;
            }

        }
        System.out.println(answer);
    }
}