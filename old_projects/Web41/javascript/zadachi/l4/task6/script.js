function getDayNameByNumber(dayNumber) {
    const daysOfWeek = [
        "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
    ];
    
    if (dayNumber < 0 || dayNumber > 6) {
        return "Invalid day number";
    }
    
    return daysOfWeek[dayNumber];
}

document.getElementById("getDayButton").addEventListener("click", function() {
    const dayInput = parseInt(document.getElementById("dayInput").value);
    const result = getDayNameByNumber(dayInput);
    document.getElementById("result").innerText = result;
});
