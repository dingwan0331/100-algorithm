function solution(array, n) {
    var answer = array.reduce((a,value,idx)=>{
        return value === n? a+1:a
    },0)
    return answer;
}