#!/usr/bin/node

const nums = process.argv;
const length = process.argv.length - 2;

if (length < 4) {
  console.log(0);
} else {
  let max = Number.NEGATIVE_INFINITY;
  let second = Number.NEGATIVE_INFINITY;

  for (let i = 2; i < length; i++) {
    if (nums[i] > max) {
      second = max;
      max = nums[i];
    }
    if (nums[i] < max && nums[i] > second) {
      second = nums[i];
    }
  }
  console.log(second);
}
