// 25. Напишите цикл, который принимает на вход два числа (A и B) и возводит число A в натуральную степень B.
/*
int DegreeOfNum(int number, int degree)
{
    int multi = number;

    for (int current = 1; current < degree; current ++)
        multi *= number;
    
    return multi;
}

Console.WriteLine("Input your number: ");
int num = Convert.ToInt32(Console.ReadLine());

Console.WriteLine("Input the degree of the number: ");
int deg = Convert.ToInt32(Console.ReadLine());

Console.WriteLine(DegreeOfNum(num, deg));
*/

// 27. Напишите программу, которая принимает на вход число и выдаёт сумму цифр в числе.
/*
int SumOfDigits(int number)
{
    int current = number;
    int digits = 0;
    int sumdigit = 0;
    while (current > 0)
    {
        sumdigit = (current % 10) + sumdigit;
        current = current / 10;
        digits ++;
    }
    return sumdigit;
}

Console.Write("Input your number: ");
int num = Convert.ToInt32(Console.ReadLine());

Console.WriteLine(SumOfDigits(num));
*/

// 29. Напишите программу, которая задаёт массив из 8 элементов и выводит их на экран.
/*
int[] AskedArray()
{
    Console.WriteLine("Input the size of your array: ");
    int size = Convert.ToInt32(Console.ReadLine());

    int[] newArray = new int[size];

    Console.WriteLine($"Input please {size} numbers: ");
    for(int i = 0; i < size; i++)
    {
        Console.Write($"Input number {i + 1}: ");
        newArray[i] = Convert.ToInt32(Console.ReadLine());
    }
    return newArray;
}

void ShowArray(int[] array)
{
    for(int i = 0; i < array.Length; i ++)
    {
        Console.Write(array[i] + " ");
    }
    Console.WriteLine();    
}

ShowArray(AskedArray());
*/