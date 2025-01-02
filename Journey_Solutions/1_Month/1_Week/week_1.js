// 1. Two Sum
var twoSum = function(nums, target) {
    const seen = {};
    for (const [i, num] of nums.entries()) {
        const diff = target - num;
        if (diff in seen) {
            return [seen[diff], i];
        }
        seen[num] = i;
    }
};

// 88. Merge Sorted Array
var merge = function(nums1, m, nums2, n) {
    let last = m + n - 1;
    let i1 = m - 1;
    let j2 = n - 1;
    while (j2 >= 0) {
        if (i1 < 0 || nums2[j2] > nums1[i1]) {
            nums1[last] = nums2[j2];
            j2 -= 1;
        }
        else {
            nums1[last] = nums1[i1];
            i1 -= 1;
        }
        last -= 1;
    }
};

// 283. Move Zeroes
var moveZeroes = function(nums) {
    let zero_i = 0;
    for (const [i, num] of nums.entries()) {
        if (num !== 0) {
            [nums[zero_i], nums[i]] = [nums[i], nums[zero_i]];
            zero_i += 1;
        }
    }
};