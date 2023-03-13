#!/usr/bin/node

const nums = process.argv;
const length = process.argv.length - 2;

if (length < 4) {
  console.log(0);
} else {
  let max = nums[2];
  let firstMax = nums[2];

  for (let i = 2; i < length; i++) {
    if (nums[length] > firstMax) {
      firstMax = nums[length];
    }
  }
  for (let j = 2; j < length; j++) {
    if (nums[length] > max && nums[length] !== firstMax) {
      max = nums[length];
    }
  }
  console.log(max);
}
