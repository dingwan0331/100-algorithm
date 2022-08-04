function solution(s) {
    var answer = '';
    let j = 0;
    for (let i =0; i<s.length; i++){
        if(s[i] == ' '){
            answer += ' '; j = 0; continue
        }
        answer += j%2 ==0 ? s[i].toUpperCase() : s[i].toLowerCase(); j++;
    }
    return answer;
}