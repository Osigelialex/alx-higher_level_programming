#!/usr/bin/node

function second (nums) {
  if (nums.length === 2 || nums.length === 3) {
    return (0);
  }

  let max = nums[2];
  let second = nums[3];
  const length = nums.length;

  for (let i = 2; i < length; i++) {
    if (nums[i] > max) {
      second = max;
      max = nums[i];
    }
    if (nums[i] < max && nums[i] > second) {
      second = nums[i];
    }
  }
  return (second);
}

console.log(second(process.argv));
