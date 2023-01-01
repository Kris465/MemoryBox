// Напишите программу, которая выводит случайное число из отрезка [10, 99] и показывает наибольшую цифру числа

/*
int FindBiggerDigit(int number)
{
    int ed = number % 10;
    int dec = number / 10;

    int max;
    if(ed > dec) max = ed;
    else max = dec;

    return max;
}

int randNumber = new Random().Next(10, 100); // Нижний предел воспринимает, верхний предел не воспринимает.
int biggerDigit = FindBiggerDigit(randNumber);

Console.WriteLine($"Bigger digit of {randNumber} is {biggerDigit}");
*/

// Напишите программу, которая выводит случайное трёхзначное число и удаляет вторую цифру этого числа.


int RemoveSecondDigit(int number)
{
    int digit1 = number / 100;
    int digit3 = number % 10;
    int result = digit1 * 10 + digit3;
    return result;
}

int randNumber = new Random().Next(100, 1000);
int completeNumber = RemoveSecondDigit(randNumber);
Console.Write($"Cut version of {randNumber} is {completeNumber}.");


// Напишите программу, которая будет принимать на вход два числа и выводить, является ли второе число кратным первому. Если второе число не кратно числу первому, то программа выводит остаток от деления.

/*
void CheckMultiplier(int number1, int number2)
{
    int rest = number2 % number1;
    if(rest == 0)
    {
        Console.WriteLine($"Второе число {number2} кратно первому число {number1}");

    }
    else
    {
        Console.WriteLine($"Второе число {number2} не кратно первому числу {number1}");
        Console.WriteLine($"Остаток от деления равен {rest}");
    }
}

Console.Write("Введите первое число ");
int num1 = Convert.ToInt32(Console.ReadLine());

Console.Write("Введите второе число ");
int num2 = Convert.ToInt32(Console.ReadLine());

CheckMultiplier(num1, num2);
*/