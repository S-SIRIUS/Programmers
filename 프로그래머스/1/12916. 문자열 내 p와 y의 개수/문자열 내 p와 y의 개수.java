class Solution {
    boolean solution(String s) {
        boolean answer = true;
        char []ch = s.toCharArray();
        int p_count = 0;
        int y_count = 0;
        for(char c: ch){
            if (Character.toUpperCase(c)=='P'){
                p_count+=1;
            }
            else if (Character.toUpperCase(c)=='Y'){
                y_count+=1;
            }
        }
        if(p_count==y_count){
            answer = true;
        }
        else{
            answer = false;
        }

        return answer;
    }
}