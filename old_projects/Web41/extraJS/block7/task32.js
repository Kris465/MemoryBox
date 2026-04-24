
const grades = [
  { exam1: 3, exam2: 2 },
  { exam1: 4, exam2: 5 },
  { exam1: 2, exam2: 3 },
  { exam1: 5, exam2: 2 },
  { exam1: 3, exam2: 4 }
];

let countFailingStudents = 0;

for (let student of grades) {
    if (student.exam1 === 2 || student.exam2 === 2) {
        countFailingStudents++;
    }
}

console.log(`Количество студентов, получивших двойку на экзамене(ах): ${countFailingStudents}`);