const fs = require("fs");

// Read data from input file
const data = fs.readFileSync("../../sample_inputs/sample_inputs.txt", "utf8");

// Split data by new line
const lines = data.split("\n");

// Create an object to track valid numbers
const trackObj = {};

// Loop through each line
for (let line of lines) {
  // Trim the line
  const trimmedLine = trimString(line);

  // Convert trimmed line to integer
  const num = convertStringToInt(trimmedLine);

  // Check if number is in range
  if (isInRange(num)) {
    // Track the number
    trackCount(num);
  }
}

// Convert trackObj values to an array
const trackObjArr = Object.values(trackObj);

// Sort the array
const sortedArr = quickSort(trackObjArr);

// Write sorted numbers to the results file
for (let num of sortedArr) {
  fs.appendFileSync("../../sample_results/sample_results.txt", num + "\n");
}

// Trim whitespace from a string
function trimString(str) {
  let newStr = "";
  for (let char of str) {
    if (char !== " ") newStr += char;
  }
  return newStr;
}

// Convert string to integer
function convertStringToInt(str) {
  return parseInt(str);
}

// Check if number is in the valid range
function isInRange(num) {
  return num >= -1023 && num <= 1023;
}

// Track the number in the trackObj object
function trackCount(num) {
  if (!trackObj[num]) trackObj[num] = num;
}

// Quick sort algorithm
function quickSort(arr) {
  if (arr.length <= 1) {
    return arr;
  }
  const pivot = arr[Math.floor(arr.length / 2)];
  const left = [];
  const right = [];

  for (let i = 0; i < arr.length; i++) {
    if (i !== Math.floor(arr.length / 2)) {
      if (arr[i] < pivot) {
        left.push(arr[i]);
      } else {
        right.push(arr[i]);
      }
    }
  }

  return quickSort(left).concat(pivot, quickSort(right));
}
