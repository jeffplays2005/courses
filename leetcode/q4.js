// 4. Median of Two Sorted Arrays

/**
 * Logic
 * I should use a 2 pointers approach to ensure that this is O(log(m+n))
 */

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function (nums1, nums2) {
  // Some base cases
  if (!nums1 || !nums2) {
    return [];
  } else if (!nums1) {
    return nums2;
  } else if (!nums2) {
    return nums1;
  }
  // starting points
  let p1 = 0;
  let p2 = 0;
  let endList = [];
  while (endList.length !== nums1.length + nums2.length) {
    if (p1 == nums1.length) {
      endList.push(...nums2.splice(p2));
      break;
    } else if (p2 == nums2.length) {
      endList.push(...nums1.splice(p1));
      break;
    }
    if (nums2[p2] < nums1[p1]) {
      // we added p2 so we need to progress the p2 pointer
      endList.push(nums2[p2]);
      p2++;
    } else {
      // we added p1 so we need to progress the p2 pointer
      endList.push(nums1[p1]);
      p1++;
    }
  }
  if (endList.length % 2 === 0) {
    // find mid 2 numbers
    const half = parseInt(endList.length / 2);
    return (endList[half - 1] + endList[half]) / 2;
  } else {
    return endList[Math.floor(endList.length / 2)];
  }
};
