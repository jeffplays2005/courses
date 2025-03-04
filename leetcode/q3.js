// 3. Longest Substring Without Repeating Characters
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  /**
   * logic:
   * Essentially keep track of the maximum size of the stack and clear all the way until the
   * character repeats again.
   *
   * [a, b, c] - > 3
   * another occurence of a!
   * a, [b, c, a] (still 3)
   */
  let longestLength = 0;
  let stack = [];
  for (let char of s) {
    // loop through the string
    if (stack.includes(char)) {
      // when the stack already has the character, we need to pop until
      stack.splice(0, stack.lastIndexOf(char) + 1);
      stack.push(char);
    } else {
      stack.push(char);
      if (stack.length > longestLength) {
        longestLength = stack.length;
      }
    }
  }
  return longestLength;
};
