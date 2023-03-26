class Solution {
    public int solution(String str1, String str2) {
        Boolean answer = str1.contains(str2);
        // return answer;
        if(answer){
            return 1;
        }
        return 2;
    }
}