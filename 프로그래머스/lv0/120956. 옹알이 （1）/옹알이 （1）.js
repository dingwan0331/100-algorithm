function solution(babbling) {
    var c = ['aya','ye','woo','ma']
    return babbling.reduce((a,b)=>{
        for(i of c){
            b  =b.replace(i,' ')
        }
        b = b.replace(' ','')
        b = b.replace(' ','')
        b = b.replace(' ','')
        b = b.replace(' ','')
        return b ? a : a+1
    },0)
}