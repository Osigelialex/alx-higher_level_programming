#!/usr/bin/node

function second(nums) {
  if (nums.length < 4) {
    return (0);
  }

  let max = Number.NEGATIVE_INFINITY;
  let second = Number.NEGATIVE_INFINITY;
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
  return(second);
}

console.log(second(process.argv));
