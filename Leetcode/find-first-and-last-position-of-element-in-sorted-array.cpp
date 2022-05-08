#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<int> search(int l, int r ,vector<int>& nums, int x) {
        if (nums.size() == 0 and x == 0){
            return {-1,-1};
        }     
        if (r >= l){
            int mid = l + (r - l)/2;
            // If element is present at the middle itself
            if (nums[mid] == x){
                l = mid;
                r = mid;
                for(int i = 0; i < nums.size(); i++ ){
                    if(nums[i] == x){
                        r = i;
                    }
                }
                for(int i = mid;i >= 0; i-- ){
                    if(nums[i] == x){
                        l = i;
                    }
                }
                return {l,r};
            }
            else{
                if(nums[mid] > x){
                    return search(l, mid-1,nums, x);

                }
                // Else the element can only be present
                // in right subarray
                else{
                    return search(mid+1,r ,nums, x);
                }
            }
        }
        else{
            // Element is not present in the array
            return {-1,-1};
        }
    }

    vector<int> searchRange (vector<int>& nums, int target){
        return this -> search(0, nums.size() - 1, nums, target);
    }

};

void print(std::vector <int> const &a) {
   cout << "The vector elements are : ";
   for(int i=0; i < a.size(); i++){
     cout << a.at(i) << ' ';  
    }
}
int main(){       
    vector<int> nums = {1,1,2}; 
    Solution x;
    auto v  = x.searchRange(nums,1);
    print(v);
    return 0; 
}


