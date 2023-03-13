#!/usr/bin/node

const nums = process.argv;
const length = process.argv.length - 2;

if (length < 4) {
  console.log(0);
} else {
  let max = nums[2];
  let second = nums[2];

  for (let i = 2; i < length; i++) {
    if (nums[length] > max) {
      secod = max;
      max = nums[i];
    }
  }
  console.log(max);
}
