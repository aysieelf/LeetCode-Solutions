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