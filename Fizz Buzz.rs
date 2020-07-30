// LeetCode Fizz Buzz
// https://leetcode.com/explore/featured/card/top-interview-questions-easy/102/math/743/

impl Solution {
    pub fn fizz_buzz(n: i32) -> Vec<String> {
        let  mut ans : Vec<String> = vec![];
        for num in 1..=n {
            
            let mut a:String = String::new();
            
            if(num % 3 == 0){
                a.push_str("Fizz");
            }
            if(num % 5 == 0){
                a.push_str("Buzz");
                
            }
            if(a.len() == 0){
                a.push_str(&num.to_string());    
            }
            ans.push(a);
        }
    ans
    }
    
}