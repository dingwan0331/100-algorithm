class Solution {
    public String solution(String bin1, String bin2) {
        String answer = "";
        Integer sum_bin;
        sum_bin = Integer.parseInt(bin1,2)+Integer.parseInt(bin2,2);
        answer = Integer.toBinaryString(sum_bin);
        return answer;
    }
}