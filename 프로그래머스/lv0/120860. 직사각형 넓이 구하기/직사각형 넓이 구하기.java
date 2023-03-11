class Solution {
    public int solution(int[][] dots) {
        int answer = 0;
        int max_x = -256;
        int max_y = -256;
        int min_x = 256;
        int min_y = 256;
        
        for (int i = 0; i < dots.length; i++){
            int x = dots[i][0];
            int y = dots[i][1];
            if (x> max_x){
                max_x = x;
            }
            if (y> max_y){
                max_y = y;
            }
            if (x < min_x){
                min_x = x;
            }
            if (y < min_y){
                min_y = y;
            }
        }
        
        int x_length = max_x - min_x;
        int y_length = max_y - min_y;
        
        return x_length*y_length;
    }
}