// 53. Maximum Subarray

var maxSubArray = function(nums) {
    let max_sum = -Infinity;
    let span = nums.length;
    while (span > 0) {
        for (let i = 0; i < nums.length; i++) {
            const l = i + span;
            if (l <= nums.length) {
                const curr_sum = nums.slice(i, l).reduce((partialSum, a) => partialSum + a, 0);
                max_sum = Math.max(max_sum, curr_sum);
            }
        }
        span -= 1;
    }
    return max_sum;
};

var maxSubArray = function(nums) {
    let current_sum = 0;
    let max_sum = -Infinity;

    for (const num of nums) {
        current_sum = Math.max(num, current_sum + num);
        max_sum = Math.max(current_sum, max_sum);
    }
    return max_sum;
};

var maxSubArray = function(nums) {
        let current_sum = 0;
    let max_sum = -Infinity;

    for (const num of nums) {
        if (current_sum + num > num) {
            current_sum += num;
        }
        else {
            current_sum = num;
        }
        if (current_sum > max_sum) {
            max_sum = current_sum;
        }
    }
    return max_sum;
};

// 66. Plus One
var plusOne = function(digits) {
    let last_i = digits.length - 1;
    let extra_one = 1;
    while (extra_one && last_i >= 0) {
        const curr_sum = digits[last_i] + 1;
        digits[last_i] = curr_sum % 10;
        extra_one = Math.floor(curr_sum / 10);
        last_i--;
    }
    if (extra_one) {
        digits.unshift(1);
    }
    return digits;
};

var plusOne = function(digits) {
    for (let i = digits.length - 1; i > -1; i--) {
        if (digits[i] < 9) {
            digits[i]++;
            return digits;
        }
        digits[i] = 0;
    }
    return [1, ...digits];
};

var plusOne = function(digits) {
    for (let i = digits.length - 1; i > -1; i--) {
        if (digits[i] < 9) {
            digits[i]++;
            return digits;
        }
        digits[i] = 0;
        if (i === 0) {
            digits.unshift(1);
            return digits;
        }
    }
};

// 26. Remove Duplicates from Sorted Array
var removeDuplicates = function(nums) {
   if (nums.length === 1) {
       return 1;
   }

   let i = 0;
   for (let j = 1; j < nums.length; j++) {
       if (nums[i] !== nums[j]) {
           i++;
           nums[i] = nums[j];
       }
   }
   return i + 1;
};