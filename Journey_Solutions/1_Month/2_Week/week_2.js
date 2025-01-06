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