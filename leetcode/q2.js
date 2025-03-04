/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
  /**
   * --- Can either create a new list and then convert that to a list node ---
   * Can create a listnode currently
   */
  let newList = [];
  let counter = 0;
  while (l1 || l2 || counter) {
    // add the two values from l1 and l2 and also the counter
    let newValue = (l1 ? l1.val : 0) + (l2 ? l2.val : 0) + counter;
    counter = 0; // reset counter once added
    if (newValue >= 10) {
      // check if overflow
      counter++; // update counter
      newValue -= 10; // set value to not overflow
    }
    newList.push(newValue);
    // progress the counter
    l1 = l1?.next;
    l2 = l2?.next;
  }
  // fine
  const out = new ListNode(newList.shift());
  let pointer = out;
  while (newList.length > 0) {
    pointer.next = new ListNode(newList.shift());
    pointer = pointer.next;
  }
  return out;
};
