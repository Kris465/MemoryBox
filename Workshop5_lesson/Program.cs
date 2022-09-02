





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
// Задайте массив. Напишите программу, которая определяет, присутствует ли заданное число в массиве. Возьмет массив и число. Тип данных - бул. 

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

// Задайте одномерный массив из 12 случайных чисел. Найдите количество элементов массива, значения которых лежат в отрезке [10,99].

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
}