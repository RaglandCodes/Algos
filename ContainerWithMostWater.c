/*
    Leetcode 11. Container With Most Water
    https://leetcode.com/problems/container-with-most-water/submissions/
*/

int min(x, y){
    if (x<y) return x;
    return y;
}

int maxArea(int* height, int heightSize){
    int l = 0,
        r = heightSize - 1,
        most_vol = 0,
        this_vol = 0;
    
    while (l<r) {
        int height_l = height[l],
            height_r = height[r];
        
        this_vol = min(height_l, height_r) * (r-l);
        
        if (this_vol > most_vol)
            most_vol = this_vol;
        
        if (height_l < height_r)
            ++l;
        else 
            --r;
    }
    
    if (this_vol > most_vol)
            most_vol = this_vol;
    
    return most_vol;
    
    
}