
/*

int[,] CreateRandom2Array(int rows, int columns, int minValue, int maxValue)
{
    int[,] newArray = new int[rows, columns];

    for(int i = 0; i < rows; i++)
    {
        for(int j = 0; j < columns; j++)
        {
            newArray[i,j] = new Random().Next(minValue, maxValue + 1);   
        }
    }
    
    return newArray;
}

void ShowArray2(int[,] array)
{
    for(int i = 0; i < array.GetLength(0); i++)
    {
        for(int j = 0; j < array.GetLength(1); j++)
            Console.Write(array[i,j] + " ");
        
        Console.WriteLine();
    }
}

Console.WriteLine("Input number of rows: ");
int m = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Input number of colums: ");
int n = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Input the min possible value: ");
int min = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Input the max possible value: ");
int max = Convert.ToInt32(Console.ReadLine());

int[,] newArray = CreateRandom2Array(m, n, min, max);
ShowArray2(newArray);

*/

// Задайте двумерный массив размера m на n, каждый элемент в массиве находится по формуле: Aij = i+j. Выведите полученный массив на экран. (показывает масив, аргументы - строки и столбцы)
/*

int[,] CreateRandom2Array(int rows, int columns)
{
    int[,] newArray = new int[rows, columns];

    for(int i = 0; i < rows; i++)
    {
        for(int j = 0; j < columns; j++)
        {
            newArray[i,j] = i + j;   
        }
    }
    
    return newArray;
}

void ShowArray2(int[,] array)
{
    for(int i = 0; i < array.GetLength(0); i++)
    {
        for(int j = 0; j < array.GetLength(1); j++)
            Console.Write(array[i,j] + " ");
        
        Console.WriteLine();
    }
}

Console.WriteLine("Input number of rows: ");
int m = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Input number of colums: ");
int n = Convert.ToInt32(Console.ReadLine());

int[,] newArray = CreateRandom2Array(m, n);
ShowArray2(newArray);
*/
// Задайте двумерный массив. Найдите элементы, у которых оба индекса чётные, и замените эти элементы на их квадраты. (массив - массив)

/*
int[,] CreateRandom2Array(int rows, int columns, int minValue, int maxValue)
{
    int[,] newArray = new int[rows, columns];

    for(int i = 0; i < rows; i++)
    {
        for(int j = 0; j < columns; j++)
        {
            newArray[i,j] = new Random().Next(minValue, maxValue + 1);   
        }
    }
    
    return newArray;
}

void ShowArray2(int[,] array)
{
    for(int i = 0; i < array.GetLength(0); i++)
    {
        for(int j = 0; j < array.GetLength(1); j++)
            if (i % 2 == 0 && j % 2 == 0)
                array[i,j] = Math.Pow(array[i,j], 2);
                Console.Write(array[i,j] + " ");
        
        Console.WriteLine();
    }
}

Console.WriteLine("Input number of rows: ");
int m = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Input number of colums: ");
int n = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Input the min possible value: ");
int min = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Input the max possible value: ");
int max = Convert.ToInt32(Console.ReadLine());

int[,] newArray = CreateRandom2Array(m, n, min, max);
ShowArray2(newArray);
*/

/*
int[,] CreateRandom2Array(int rows, int columns, int minValue, int maxValue)
{
    int[,] newArray = new int[rows, columns];

    for(int i = 0; i < rows; i++)
    {
        for(int j = 0; j < columns; j++)
        {
            newArray[i,j] = new Random().Next(minValue, maxValue + 1);   
        }
    }
    
    return newArray;
}

void ShowArray2(int[,] array)
{
    for(int i = 0; i < array.GetLength(0); i++)
    {
        for(int j = 0; j < array.GetLength(1); j++)
            Console.Write(array[i,j] + " ");
        
        Console.WriteLine();
    }
}

int[,] Switch (int[,] array)
{
    for(int i = 0; i < array.GetLength(0); i++)
    {
        for(int j = 0; j < array.GetLength(1); i++)
        {
            if (i % 2 == 0 && j % 2 == 0) array[i,j] = array[i,j] * array[i,j];
        }
    }

    return array;
}


Console.WriteLine("Input number of rows: ");
int m = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Input number of colums: ");
int n = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Input the min possible value: ");
int min = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Input the max possible value: ");
int max = Convert.ToInt32(Console.ReadLine());

int[,] newArray = CreateRandom2Array(m, n, min, max);
ShowArray2(newArray);
Console.WriteLine();
int[,] switchArray = Switch(newArray);
ShowArray2(switchArray);
*/

// Задайте двумерный массив. Найдите сумму элементов, находящихся на главной диагонали (с индексами (0,0); (1;1) и т.д. (целочисленный двумерный массив, на выходе - просто int)

/*
int[,] CreateRandom2Array(int rows, int columns, int minValue, int maxValue)
{
    int[,] newArray = new int[rows, columns];

    for(int i = 0; i < rows; i++)
    {
        for(int j = 0; j < columns; j++)
        {
            newArray[i,j] = new Random().Next(minValue, maxValue + 1);   
        }
    }
    
    return newArray;
}

void ShowArray2(int[,] array)
{
    for(int i = 0; i < array.GetLength(0); i++)
    {
        for(int j = 0; j < array.GetLength(1); j++)
            Console.Write(array[i,j] + " ");
        
        Console.WriteLine();
    }
}

int SumUp(int[,] array)
{
    int sum = 0;
    for (int i = 0; i < array.GetLength(0); i ++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            if (i == j) sum += array[i, j];
        }
    }

    return sum;
}

Console.WriteLine("Input number of rows: ");
int m = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Input number of colums: ");
int n = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Input the min possible value: ");
int min = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Input the max possible value: ");
int max = Convert.ToInt32(Console.ReadLine());

int[,] newArray = CreateRandom2Array(m, n, min, max);
ShowArray2(newArray);
Console.WriteLine();
int sum = SumUp(newArray);
Console.WriteLine($" {sum} ");
*/

/*
int a = 5;
ShowNum(a);
Console.WriteLine(a);

int[] arr = {3, 15, 7};
ChangeArray(arr);
Console.WriteLine(arr[0]);

void ShowNum(int num)
{
    num += 5;
    Console.WriteLine(num);
}

void ChangeArray(int[] array)
{
    array[0] += 5;
    Console.WriteLine(array[0]);
}
*/


int[,] CreateRandom2Array(int rows, int columns, int minValue, int maxValue)
{
    int[,] newArray = new int[rows, columns];

    for(int i = 0; i < rows; i++)
    {
        for(int j = 0; j < columns; j++)
        {
            newArray[i,j] = new Random().Next(minValue, maxValue + 1);   
        }
    }
    
    return newArray;
}

void ShowArray2(int[,] array)
{
    for(int i = 0; i < array.GetLength(0); i++)
    {
        for(int j = 0; j < array.GetLength(1); j++)
            Console.Write(array[i,j] + " ");
        
        Console.WriteLine();
    }
}

int FindSum (int[,] array)
{
    int sum = 0;
    for(int i = 0; i < array.GetLength(0) && i < array.GetLength(1); i++)
        sum += array[i,i];

    return sum;
}

Console.WriteLine("Input number of rows: ");
int m = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Input number of colums: ");
int n = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Input the min possible value: ");
int min = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Input the max possible value: ");
int max = Convert.ToInt32(Console.ReadLine());

int[,] newArray = CreateRandom2Array(m, n, min, max);
ShowArray2(newArray);
Console.WriteLine();
int sum = FindSum(newArray);
Console.WriteLine($"Сумма элементов главной диагонали равна {sum}.");