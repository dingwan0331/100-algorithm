fun main(args: Array<String>) {
    val s1: String = readLine()!!
    var answer: String = ""
    for (i in s1)
        if (i.isLowerCase()){
            answer += i.toUpperCase()
        }else{
            answer += i.toLowerCase()
        }
    
    print(answer)
}