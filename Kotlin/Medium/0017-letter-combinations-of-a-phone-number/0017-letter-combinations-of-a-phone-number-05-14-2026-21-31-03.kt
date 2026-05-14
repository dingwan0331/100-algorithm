class Solution {
// 1. 숫자별 문자 매핑 정의
    private val digitToLetters = mapOf(
        '2' to "abc", '3' to "def", '4' to "ghi", '5' to "jkl",
        '6' to "mno", '7' to "pqrs", '8' to "tuv", '9' to "wxyz"
    )

    fun letterCombinations(digits: String): List<String> {
        // 예외 처리: 입력값이 비어있으면 빈 리스트 반환
        if (digits.isEmpty()) return emptyList()

        val result = mutableListOf<String>()
        
        // 2. 백트래킹 함수 호출
        backtrack(result, StringBuilder(), digits, 0)
        
        return result
    }

    private fun backtrack(
        result: MutableList<String>,
        current: StringBuilder,
        digits: String,
        index: Int
    ) {
        // 기저 조건: 모든 숫자를 다 확인했을 때 결과 리스트에 추가
        if (index == digits.length) {
            result.add(current.toString())
            return
        }

        // 현재 인덱스의 숫자에 해당하는 문자열 가져오기
        val letters = digitToLetters[digits[index]] ?: ""
        
        for (char in letters) {
            current.append(char)           // 문자를 추가하고
            backtrack(result, current, digits, index + 1) // 다음 숫자로 이동
            current.deleteCharAt(current.length - 1) // 백트래킹 (마지막 문자 제거)
        }
    }
}