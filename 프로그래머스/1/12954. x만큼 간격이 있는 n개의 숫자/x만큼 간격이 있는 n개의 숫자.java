class Solution {
    public long[] solution(int x, int n) {
        long[] answer = new long[n];
        
        int count =0;
        long data=x;
        while(n>0){
            answer[count]=data;
            data+=x;
            count+=1;
            n-=1;
        }
        
        return answer;
    }
}