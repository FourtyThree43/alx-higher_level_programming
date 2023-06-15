#!/usr/bin/node

function findCombinations(x, currentExpression, currentResult, index) {
  if (index === x.length) {
    if (currentResult === parseInt(x, 10)) {
      console.log(currentExpression);
    }
    return;
  }

  let currentNumber = '';

  for (let i = index; i < x.length; i++) {
    currentNumber += x[i];
    const number = parseInt(currentNumber, 10);

    if (currentExpression === '') {
      findCombinations(x, currentExpression + number, number, i + 1);
    } else {
      findCombinations(x, currentExpression + '+' + number, currentResult + number, i + 1);
      findCombinations(x, currentExpression + '-' + number, currentResult - number, i + 1);
      findCombinations(x, currentExpression + '*' + number, currentResult * number, i + 1);
      findCombinations(x, currentExpression + '/' + number, currentResult / number, i + 1);
    }

    // Handle cases where multiple digits are combined (e.g., 1 and 2 become 12)
    if (x[index] === '0') {
      break;
    }
  }
}

function findPossibleCombinations(targetNumber) {
  const x = targetNumber.toString();
  findCombinations(x, '', 0, 0);
}

const targetNumber = parseInt(process.argv[2], 10);
findPossibleCombinations(targetNumber);
