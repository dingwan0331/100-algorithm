class Solution {
    public int solution(String A, String B) {
        
        for (int i=0; i < A.length(); i++){
            int idx = A.length() - i;
            String a = A.substring(0,idx);
            String b = A.substring(idx);
            String C = b.concat(a);
            String D = a.concat(b);
            if( C.equals(B) || D.equals(B)){
                return i;
            }
        }
        return -1;
    }
}