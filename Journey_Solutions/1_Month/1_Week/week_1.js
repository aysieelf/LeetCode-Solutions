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

// 1480. Running Sum of 1d Array
var runningSum = function(nums) {
    const result = [nums[0]];
    for (let i = 1; i < nums.length; i++) {
        result.push(result[result.length - 1] + nums[i]);
    }
    return result;
};

// 217. Contains Duplicate
var containsDuplicate = function(nums) {
  const seen = new Set();
  for (const num of nums) {
      if (seen.has(num)) {
          return true;
      }
      seen.add(num);
  }
  return false;
};

var containsDuplicate2 = function(nums) {
    return new Set(nums).size !== nums.length;
};

var containsDuplicate3 = function (nums) {
    nums.sort();
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] === nums[i-1]) {
            return true;
        }
    }
    return false;
};