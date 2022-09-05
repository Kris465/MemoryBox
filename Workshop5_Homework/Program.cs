// Задайте массив заполненный случайными положительными трёхзначными числами. Напишите программу, которая покажет количество чётных чисел в массиве.

/*
int[] CreateRandomArray(int size)
{
    int[] newArray = new int[size];

    for(int i = 0; i < size; i++)
        newArray[i] = new Random().Next(100, 999 + 1);

    return newArray;
}

void ShowArray(int[] array)
{
    int count = 0;
    for(int i = 0; i < array.Length; i ++)
    {
        Console.Write(array[i] + " ");
        if (array[i] % 2 == 0) count++;
    }
    Console.WriteLine($"\nThere are {count} even numbers!");    
}

Console.WriteLine("Input the size of a random array: ");
int si = Convert.ToInt32(Console.ReadLine());
ShowArray(CreateRandomArray(si));
*/

// Задайте одномерный массив, заполненный случайными числами. Найдите сумму элементов, стоящих на нечётных позициях.
/*
int[] CreateRandomArray(int size, int minValue, int maxValue)
{
    int[] newArray = new int[size];

    for(int i = 0; i < size; i++)
        newArray[i] = new Random().Next(minValue, maxValue + 1);

    return newArray;
}

void ShowArray(int[] array)
{
    int sum = 0;
    for(int i = 0; i < array.Length; i++)
    {
        Console.Write(array[i] + " ");
        if (i % 2 == 1) sum += array[i];
    }
    Console.WriteLine($"\n The sum is {sum}!");    
}

Console.WriteLine("Input the size of random array, low limit, upper limit: ");
int si = Convert.ToInt32(Console.ReadLine());
int min = Convert.ToInt32(Console.ReadLine());
int max = Convert.ToInt32(Console.ReadLine());
ShowArray(CreateRandomArray(si, min, max));
*/

// Задайте массив вещественных чисел. Найдите разницу между максимальным и минимальным элементов массива. NextDouble() - не принимает аргументов. Генерирует случайное вещественное числов в диапазоне от нуля до единицы. Сумма next + next double. double[] - массив вещественных чисел.

double[] CreateRandomArray(int size, int minValue, int maxValue)
{
    double[] newArray = new double[size];

    for(int i = 0; i < size; i++)
        newArray[i] = Math.Round(new Random().NextDouble(), 2) + new Random().Next(minValue, maxValue + 1);

    return newArray;
}

void ShowArray(double[] array)
{
    double min = array[0];
    double max = array[0];
    for(int i = 0; i < array.Length; i ++)
    {
        Console.Write(array[i] + " ");
        if (array[i] > max) max = array[i]; 
        if (array[i] < min) min = array[i];
    }
    Console.WriteLine($"\nThe diffenece between {max} and {min} is {max - min}.");
}

Console.WriteLine("Input the size of random array, low limit, upper limit: ");
int si = Convert.ToInt32(Console.ReadLine());
int min = Convert.ToInt32(Console.ReadLine());
int max = Convert.ToInt32(Console.ReadLine());
ShowArray(CreateRandomArray(si, min, max));