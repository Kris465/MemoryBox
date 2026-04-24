const prompt = require('prompt-sync')();

const classrooms = [
    { name: 'Аудитория 101', seats: 15, faculty: 'Факультет Информационных Технологий' },
    { name: 'Аудитория 102', seats: 10, faculty: 'Факультет Искусств' },
    { name: 'Аудитория 201', seats: 20, faculty: 'Факультет Математики' },
    { name: 'Аудитория 202', seats: 18, faculty: 'Факультет Информационных Технологий' },
    { name: 'Аудитория 203', seats: 12, faculty: 'Факультет Искусств' },
    { name: 'Аудитория 301', seats: 17, faculty: 'Факультет Математики' },
];


function displayAllClassrooms() {
    console.log("Все аудитории:");
    classrooms.forEach(classroom => {
        console.log(`Название: ${classroom.name}, Мест: ${classroom.seats}, Факультет: ${classroom.faculty}`);
    });
}


function displayClassroomsByFaculty(faculty) {
    console.log(`Аудитории для факультета "${faculty}":`);
    const filteredClassrooms = classrooms.filter(classroom => classroom.faculty === faculty);
    filteredClassrooms.forEach(classroom => {
        console.log(`Название: ${classroom.name}, Мест: ${classroom.seats}`);
    });
}


function displayClassroomsForGroup(group) {
    console.log(`Аудитории для группы "${group.name}":`);
    const suitableClassrooms = classrooms.filter(classroom => 
        classroom.seats >= group.numberOfStudents && classroom.faculty === group.faculty
    );
    suitableClassrooms.forEach(classroom => {
        console.log(`Название: ${classroom.name}, Мест: ${classroom.seats}`);
    });
}


function sortClassroomsBySeats() {
    const sortedClassrooms = [...classrooms].sort((a, b) => a.seats - b.seats);
    console.log("Аудитории отсортированные по количеству мест:");
    sortedClassrooms.forEach(classroom => {
        console.log(`Название: ${classroom.name}, Мест: ${classroom.seats}`);
    });
}


function sortClassroomsByName() {
    const sortedClassrooms = [...classrooms].sort((a, b) => a.name.localeCompare(b.name));
    console.log("Аудитории отсортированные по названию:");
    sortedClassrooms.forEach(classroom => {
        console.log(`Название: ${classroom.name}, Мест: ${classroom.seats}`);
    });
}

displayAllClassrooms();
displayClassroomsByFaculty('Факультет Информационных Технологий');
displayClassroomsForGroup({ name: 'Группа 1', numberOfStudents: 15, faculty: 'Факультет Информационных Технологий' });
sortClassroomsBySeats();
sortClassroomsByName();

