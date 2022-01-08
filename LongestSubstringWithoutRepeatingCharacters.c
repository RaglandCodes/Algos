/*

LeetCode 3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

*/

int lengthOfLongestSubstring(char * s){
    int ptr_1 = 0,
        ptr_2 = 0,
        hash[128], // ASCII has 128 characters
        i; 
    
    memset(hash, 0, 128*sizeof(int));
    
    if(!s[ptr_1])
        return 0;
    
    hash[s[ptr_1]] = 1;
    
    bool isValidWindow(){
        i = 0;
        while(i<128)
            if(hash[i++]>1)
                return false;
        
        return true;
    }
    
    while(s[++ptr_2]){
        ++hash[s[ptr_2]];
        
        if (!isValidWindow())           
            --hash[s[ptr_1++]];

    }
    
    return ptr_2 - ptr_1;
}