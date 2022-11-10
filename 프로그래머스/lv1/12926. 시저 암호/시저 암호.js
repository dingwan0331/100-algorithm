function solution(s, n) {
    const lower = 97
    const upper = 65
    
    var answer = '';
    for (let i=0;i<s.length;i++){
        let a = ''
        if (s[i] === ' '){
            a = ' '
        }
        else if (s[i].match(/[a-z]/g)){
            a = String.fromCharCode(lower + (s[i].charCodeAt(0) + n - lower) % 26)
        }else{
            a = String.fromCharCode(upper + (s[i].charCodeAt(0) + n - upper) % 26)
        }
        answer += a
    }
    return answer;
}