#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

// take advantage of the sorted property
// iterate through the array with two pointers
// make greedy choices based on the sum
vector<int> twoSum(vector<int>& numbers, int target) {
    int n = numbers.size();
    int idx1 = 0;
    int idx2 = n - 1;
    int sum;
    while (idx1 < idx2) {
        sum = numbers[idx1] + numbers[idx2];
        if (sum == target) {
            return {idx1 + 1, idx2 + 1};
        }
        else if (sum > target) {
            idx2--;
        }
        else {
            idx1++;
        }
    }
    return {-1};
}

int main() {
	vector<int> numbers = {2, 7, 11, 15};
	int target = 9;
	vector<int> result = twoSum(numbers, target);
	for (int idx : result) {
		cout << idx << " ";
	}
	return 0;
}