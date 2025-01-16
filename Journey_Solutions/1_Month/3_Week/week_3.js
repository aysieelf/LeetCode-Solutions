// 242. Valid Anagram

var isAnagram = function(s, t) {
    if (s.length !== t.length) {
        return false;
    }
    const seen = {};

    for (const ls of s) {
        if (ls in seen) {
            seen[ls] += 1;
        }
        else {
            seen[ls] = 1;
        }
    }

    for (const lt of t) {
        seen[lt] -= 1;
    }

    for (const key in seen) {
        if (seen[key] !== 0) {
            return false;
        }
    }
    return true;
};

var isAnagram = function(s, t) {
    if (s.length !== t.length) {
        return false;
    }
    s = s.split("").sort()
    t = t.split("").sort()

    for (let i = 0; i < s.length; i++) {
        if (s[i] !== t[i]) {
            return false;
        }
    }
    return true;
};

// 125. Valid Palindrome
var isPalindrome = function(s) {
    s = s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();

    let left = 0;
    let right = s.length - 1;

    while (left < right) {
        if (s[left] !== s[right]) return false;
        left++;
        right--;
    }

    return true;
};

// 344. Reverse String
var reverseString = function(s) {
    for (let i = 0; i < Math.floor(s.length) / 2; i++) {
        [s[i], s[s.length - 1 - i]] = [s[s.length - 1 - i], s[i]];
    }
};

// 387. First Unique Character in a String
var firstUniqChar = function(s) {
    const seen = {};

    for (let i = 0; i < s.length; i++) {
        if (s[i] in seen) {
            seen[s[i]] = -1;
        }
        else {
            seen[s[i]] = i;
        }
    }

    for (const v of Object.values(seen)) {
        if (v !== -1) {
            return v;
        }
    }
    return -1;
};
