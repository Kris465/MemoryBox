/*
int FindSum(int num)
{
    int sum = 0;

    for (int current = 1; current <= num; current ++)
        sum += current;

    return sum;
}

Console.Write("Input positive integer number: ");
int a = Convert.ToInt32(Console.ReadLine());

Console.WriteLine($"Sum of numbers from 1 to {a} is {FindSum(a)}");
*/

// Напишите программу, которая принимает на вход число и выдаёт количество цифр в числе.
/*
int AmountOfNumbers(int number)
{
    int current = number;
    int output = 0;
    while (current > 0)
    {
        current = current / 10;
        output ++;
    }
    return output;
}

Console.Write("Input your number: ");
int num = Convert.ToInt32(Console.ReadLine());

Console.WriteLine(AmountOfNumbers(num));
*/

// Напишите программу, которая принимает на вход число N и выдаёт произведение чисел от 1 до N.
/*
int FindFact(int num)
{
    int sum = 1;

    for (int current = 1; current <= num; current ++)
        sum *= current;

    return sum;
}

Console.Write("Input positive integer number: ");
int a = Convert.ToInt32(Console.ReadLine());

Console.WriteLine($"Sum of numbers from 1 to {a} is {FindFact(a)}");
*/

// Напишите программу, которая выводит массив из 8 элементов, заполненный нулями и единицами в случайном порядке.
/*
void FillArray(int[] collection)
{
    int length = collection.Length;
    int index = 0;
    while (index < length)
    {
        collection[index] = new Random().Next(0, 2);
        index ++;

    }

}

void PrintArray(int[] col)
{
    int count = col.Length;
    int position = 0;
    while (position < count)
    {
        Console.Write(col[position] + " ");
        position ++;
    }
}

int[] array = new int[8];

FillArray(array);
PrintArray(array);
*/


int[] CreateRandomArray(int size, int minValue, int maxValue) // Генерирует любой рандомный массив. 
{
    int[] newArray = new int[size];

    for(int i = 0; i < size; i++) //i = i + 2
        newArray[i] = new Random().Next(minValue, maxValue + 1);

    return newArray;
}

void ShowArray(int[] array)
{
    for(int i = 0; i < array.Length; i ++)
        Console.Write(array[i] + " ");

    Console.WriteLine();    
}

// ShowArray(CreateRandomArray(8, 0, 1));
ShowArray(CreateRandomArray(25, 0, 9));