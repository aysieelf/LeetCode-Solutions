// 389. Find the Difference
var findTheDifference = function(s, t) {
    let result = 0;

    for (const char of s) {
        result ^= char.charCodeAt(0);
    }

    for (const char of t) {
        result ^= char.charCodeAt(0);
    }

    return String.fromCharCode(result);
};

// 349. Intersection of Two Arrays
var intersection = function(nums1, nums2) {
    if (nums1.length > nums2.length) {
        [nums1, nums2] = [nums2, nums1];
    }
    const set1 = new Set(nums1);
    return [...new Set(nums2.filter(num => set1.has(num)))];
};

// 290. Word Pattern
var wordPattern = function(pattern, s) {
    const words = s.split(' ');
    if (pattern.length !== words.length) {
        return false;
    }

    const map = new Map();
    const map2 = new Map();

    for (let i = 0; i < pattern.length; i++) {
        if (map.has(pattern[i]) && map.get(pattern[i]) !== words[i]) {
            return false;
        }
        if (map2.has(words[i]) && map2.get(words[i]) !== pattern[i]) {
            return false;
        }
        map.set(pattern[i], words[i]);
        map2.set(words[i], pattern[i]);
    }
    return true;
}