import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        
        return String.valueOf(n).chars().map(c -> c - '0').sum();
    }
}