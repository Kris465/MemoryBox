const prompt = require('prompt-sync')();

let classrooms = [
    { name: "Аудитория 101", seats: 15, faculty: "Факультет информатики" },
    { name: "Аудитория 102", seats: 20, faculty: "Факультет математики" },
    { name: "Аудитория 103", seats: 12, faculty: "Факультет физики" },
    { name: "Аудитория 104", seats: 10, faculty: "Факультет информатики" },
    { name: "Аудитория 105", seats: 18, faculty: "Факультет биологии" }
];

function displayAllClassrooms() {
    console.log("\nВсе аудитории:");
    classrooms.forEach(classroom => {
        console.log(`Название: ${classroom.name}, Мест: ${classroom.seats}, Факультет: ${classroom.faculty}`);
    });
}

function displayClassroomsByFaculty(faculty) {
    console.log(`\nАудитории для факультета "${faculty}":`);
    const filteredClassrooms = classrooms.filter(classroom => classroom.faculty === faculty);
    if (filteredClassrooms.length > 0) {
        filteredClassrooms.forEach(classroom => {
            console.log(`Название: ${classroom.name}, Мест: ${classroom.seats}`);
        });
    } else {
        console.log("Нет аудиторий для указанного факультета.");
    }
}

function displaySuitableClassrooms(group) {
    console.log(`\nАудитории, подходящие для группы "${group.name}":`);
    const suitableClassrooms = classrooms.filter(classroom => classroom.seats >= group.students && classroom.faculty === group.faculty);
    if (suitableClassrooms.length > 0) {
        suitableClassrooms.forEach(classroom => {
            console.log(`Название: ${classroom.name}, Мест: ${classroom.seats}`);
        });
    } else {
        console.log("Нет подходящих аудиторий для данной группы.");
    }
}

function sortClassroomsBySeats() {
    classrooms.sort((a, b) => a.seats - b.seats);
    console.log("\nАудитории отсортированы по количеству мест:");
    displayAllClassrooms();
}

function sortClassroomsByName() {
    classrooms.sort((a, b) => a.name.localeCompare(b.name));
    console.log("\nАудитории отсортированы по названию:");
    displayAllClassrooms();
}

while (true) {
    console.log("\nВыберите действие:");
    console.log("1. Вывести все аудитории");
    console.log("2. Вывести аудитории для указанного факультета");
    console.log("3. Вывести аудитории, подходящие для группы");
    console.log("4. Отсортировать аудитории по количеству мест");
    console.log("5. Отсортировать аудитории по названию");
    console.log("6. Выйти");

    const choice = prompt("Ваш выбор: ");

    switch (choice) {
        case '1':
            displayAllClassrooms();
            break;
        case '2':
            const faculty = prompt("Введите название факультета: ");
            displayClassroomsByFaculty(faculty);
            break;
        case '3':
            const groupName = prompt("Введите название группы: ");
            const groupStudents = parseInt(prompt("Введите количество студентов: "), 10);
            const groupFaculty = prompt("Введите название факультета группы: ");
            const group = { name: groupName, students: groupStudents, faculty: groupFaculty };
            displaySuitableClassrooms(group);
            break;
        case '4':
            sortClassroomsBySeats();
            break;
        case '5':
            sortClassroomsByName();
            break;
        case '6':
            console.log("Выход из программы...");
            process.exit();
            break;
        default:
            console.log("Неверный выбор. Пожалуйста, попробуйте снова.");
    }
}
