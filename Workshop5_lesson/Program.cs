// Задайте массив из 12 элементов, заполненный случайными числами из промежутка [-9, 9]. Найдите сумму отрицательных и положительных элементов массива.
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
    for(int i = 0; i < array.Length; i ++)
        Console.Write(array[i] + " ");

    Console.WriteLine();    
}

int FindPositiveSum(int[] array)
{
    int sum = 0;
    
    for (int i = 0; i < array.Length; i++)
        if(array[i] > 0) sum += array[i]; // sum = sum + array[i];

    return sum;
}


int FindNegativeSum(int[] array)
{
    int sum = 0;
    
    for (int i = 0; i < array.Length; i++)
        if(array[i] < 0) sum += array[i];

    return sum;
}

// int[] arr = CreateRandomArray(23,-10,20);
// ShowArray(arr);
// int sum1 = FindPositiveSum(arr);
// int sum2 = FindNegativeSum(arr);
// Console.WriteLine($"{sum1}, {sum2} ");

Console.Write("Input size of array: ");
int size = Convert.ToInt32(Console.ReadLine());
Console.Write("Input min possible value: ");
int min = Convert.ToInt32(Console.ReadLine());
Console.Write("Input max possible value: ");
int max = Convert.ToInt32(Console.ReadLine());

int[] myArray = CreateRandomArray(size, min, max);
ShowArray(myArray);

int positiveSum = FindPositiveSum(myArray);
int negativeSum = FindNegativeSum(myArray);

Console.WriteLine($"Sum of positive elements is {positiveSum} \nSum of negative elements is {negativeSum}");
*/

// Напишите программу замена элементов массива: положительные элементы замените на соответствующие отрицательные, и наоборот. Возьмет на вход массив, перевернет элементы с отрицательных на положительные и наоборот и вернет новый массив.
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
    for(int i = 0; i < array.Length; i ++)
        Console.Write(array[i] + " ");

    Console.WriteLine();    
}

int[] ChangeArray(int[] array)
{

    for(int i = 0; i < array.Length; i ++)
        array[i] = array[i] * -1;
    return array;
}

int[] array1 = CreateRandomArray(25, -9, 9);
ShowArray(array1);
ShowArray(ChangeArray(array1));
*/

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
    for(int i = 0; i < array.Length; i ++)
        Console.Write(array[i] + " ");

    Console.WriteLine();    
}

int[] Swap(int[] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        array[i] *= (-1);
    }
    return array;
}

 int[] arr = CreateRandomArray(10, -19, 23);
 ShowArray(arr);
 ShowArray(Swap(arr));
*/

// Задайте массив. Напишите программу, которая определяет, присутствует ли заданное число в массиве. Возьмет массив и число. Тип данных - бул. 
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
    for(int i = 0; i < array.Length; i ++)
        Console.Write(array[i] + " ");

    Console.WriteLine();    
}

int[] CreateRandomArray(int size, int minValue, int maxValue)
{
    int[] newArray = new int[size];

    for(int i = 0; i < size; i++) 
        newArray[i] = new Random().Next(minValue, maxValue + 1);

    return newArray;
}

void ShowArray(int[] array)
{
    for(int i = 0; i < array.Length; i ++)
        Console.Write(array[i] + " ");

    Console.WriteLine();    
}

bool FindNumber(int[] array, int number)
{
    for(int i = 0; i < array.Length; i ++)
        if (array[i] == number) return true;
    return false;
}

int[] array1 = CreateRandomArray(25, -9, 9);
ShowArray(array1);

Console.WriteLine("Input your number: ");
int num = Convert.ToInt32(Console.ReadLine());
Console.WriteLine(FindNumber(array1, num));
*/

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
    for(int i = 0; i < array.Length; i ++)
        Console.Write(array[i] + " ");

    Console.WriteLine();    
}

bool NumCheck(int[] array)
{
    int urnum = Convert.ToInt32(Console.ReadLine());

    for (int i = 0; i < array.Length; i ++)
    {
        if (urnum == array[i])
            return true;
    }
    return false;
}

Console.WriteLine("Input your number: ");
int[] arr = CreateRandomArray(15, -8, 17);
ShowArray(arr);
Console.WriteLine($"{NumCheck(arr)}");
*/

// Задайте одномерный массив из 12 случайных чисел. Найдите количество элементов массива, значения которых лежат в отрезке [10,99].
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
    for(int i = 0; i < array.Length; i ++)
        Console.Write(array[i] + " ");

    Console.WriteLine();    
}

int Amount(int[] array)
{
    int amount = 0;
    
    for (int i = 0; i < array.Length; i ++)
        if (array[i] >= 10 && array[i] <= 99) amount ++;
    return amount;
}

int[] arr = CreateRandomArray(12, -7, 150);
ShowArray(arr);
Console.WriteLine(Amount(arr));
*/

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
    for(int i = 0; i < array.Length; i ++)
        Console.Write(array[i] + " ");

    Console.WriteLine();    
}

int DoubleDigit(int[] array)
{
    int current = 0;
    for (int i = 0; i < array.Length; i ++)
    {
        if (array[i] > 10 && array[i] < 100) current ++;
    }
    return current;
}

int[] arr = CreateRandomArray(12, -7, 150);
ShowArray(arr);
Console.WriteLine(DoubleDigit(arr));
*/