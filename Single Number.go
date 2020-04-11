`

LeetCode 136. Single Number
https://leetcode.com/problems/single-number/submissions/

`
func singleNumber(nums []int) int {

    a := 0
    for _, e := range nums {
        fmt.Println(e)
        a ^= e
    }
    return a
}