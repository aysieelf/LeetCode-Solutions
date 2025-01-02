// 1. Two Sum
var twoSum = function(nums, target) {
    const seen = {};
    for (const [i, num] of nums.entries()) {
        const diff = target - num
        if (diff in seen) {
            return [seen[diff], i]
        }
        seen[num] = i
    }
};

//