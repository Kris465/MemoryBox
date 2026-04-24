function countFivesCase1(grades) {
  const firstNonFiveIndex = grades.findIndex(grade => grade !== 5);
  return firstNonFiveIndex === -1 ? 0 : firstNonFiveIndex;
}

const grades1 = [5, 5, 5, 4, 3, 5, 2];
console.log(countFivesCase1(grades1)); 