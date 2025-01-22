// 680. Valid Palindrome II
var validPalindrome = function(s) {
    let l = 0;
    let r = s.length - 1;

    while (l < r) {
        if (s[l] !== s[r]) {
            const firstCase = s.slice(l+1, r+1);
            const secondCase = s.slice(l, r);

            return ((
                firstCase === reverseCase(firstCase)) ||
                (secondCase === reverseCase(secondCase))
                );
        }
        l++;
        r--;
    }
    return true;
};

function  reverseCase(str) {
    return str.split('').reverse().join('');
}

// 28. Find the Index of First Occurrence in a String
var strStr = function(haystack, needle) {
    if (haystack.length < needle.length) {
        return -1;
    }

    for (let i = 0; i < haystack.length; i++) {
        if (haystack.slice(i, i + needle.length) === needle) {
            return i;
        }
    }
    return -1;
};


// 448. Find All Numbers
var findDisappearedNumbers = function(nums) {
    const nums_set = new Set(nums);
    const result = [];

    for (let i = 1; i < nums.length + 1; i++) {
        if (!nums_set.has(i)) {
            result.push(i);
        }
    }
    return result;
};