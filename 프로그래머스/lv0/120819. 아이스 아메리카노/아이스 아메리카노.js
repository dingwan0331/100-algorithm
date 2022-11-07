function solution(money) {
    var answer = [0, money];
    while (answer[1] >= 5500){
        answer[1] -= 5500
        answer[0] += 1
    }
    return answer;
}