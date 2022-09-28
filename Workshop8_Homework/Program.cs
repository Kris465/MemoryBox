// Задайте двумерный массив. Напишите программу, которая упорядочит по убыванию элементы каждой строки двумерного массива.
/*
int[,] CreateRandom2Array()
{
    Console.WriteLine("Input number of rows: ");
    int rows = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine("Input number of colums: ");
    int columns = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine("Input the min possible value: ");
    int minValue = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine("Input the max possible value: ");
    int maxValue = Convert.ToInt32(Console.ReadLine());

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
    Console.WriteLine();
}

*/

/*
int[,] SortedArray(int[,] array)
{
    int[,] newArray = array;

    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1) - 1; j++)
        {
            for (int line = 0; line > i; line++)
            {
                if (array[line, j] < array[i,j])
                {
                    int temp = array[line,j];
                    array[line,j] = array[i, j];
                    array[i, j] = temp;
                }
            }
        }
    }
    return newArray;
}
*/

/*
int j = 0;

int SortedArray(int[,] array, int column)
{
    int[,] newArray = array;
    int max = array[0,0];

    for (int i = 0; i < newArray.GetLength(0); i++)
    {
        newArray[i,j] > newArray[i + 1, j];
        int temp = array[line,j];
        array[line,j] = array[i, j];
        array[i, j] = temp;
    }
    return j;
}

*/

/*
int[,] SortedArray(int[,] array)
{
    int[,] newArray = new int[array.GetLength(0),array.GetLength(1)];
    int max = 0;
    int current = 0;

    for(int i = 0; i < array.GetLength(0); i++)
    {
        for(int j = 0; j < array.GetLength(1); j++)
        {
            if (i == current)
            {
                if (array[i, j] < array[i, j + 1])
                {
                    int temp = array[i,j]
                } 
            }
        }
            
        
        Console.WriteLine();
    }
    Console.WriteLine();
    return newArray[,];
}

int[,] myArray = CreateRandom2Array();
ShowArray2(myArray);
SortedArray(myArray, j);
ShowArray2(myArray);
*/

/*
int[,] CreateRandom2Array()
{
    Console.WriteLine("Input number of rows: ");
    int rows = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine("Input number of colums: ");
    int columns = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine("Input the min possible value: ");
    int minValue = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine("Input the max possible value: ");
    int maxValue = Convert.ToInt32(Console.ReadLine());

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
    Console.WriteLine();
}

void SortedArray(int[,] array, int row)
{
    for (int j = 0; j < array.GetLength(1) - 1; j ++)
    {
        for (int k = j + 1; k < array.GetLength(1); k++)
        {    
            if (array[row, j] < array[row, k])                  
            {                                               
                int temp = array[row, j];
                array[row, j] = array[row, k];
                array[row, k] = temp;
            }
        }       
    }

    if (row < array.GetLength(0)-1)
        SortedArray(array, row + 1);
}


int[,] myArray = CreateRandom2Array();
ShowArray2(myArray);
SortedArray(myArray, 0);
ShowArray2(myArray);
*/ 

// Задайте прямоугольный двумерный массив. Напишите программу, которая будет находить строку с наименьшей суммой элементов.

/*
int[,] CreateRandom2Array()
{
    Console.WriteLine("Input number of rows: ");
    int rows = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine("Input number of colums: ");
    int columns = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine("Input the min possible value: ");
    int minValue = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine("Input the max possible value: ");
    int maxValue = Convert.ToInt32(Console.ReadLine());

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
    Console.WriteLine();
}

void LineOfMin(int[,] array) 
{
    int row = 0;
    int min = 0; 
    for(int j = 0; j < array.GetLength(1); j++)
        min = array[0, j] + min;   

    for(int i = 0; i < array.GetLength(0); i++)
    {
        int sum = 0;
        for(int j = 0; j < array.GetLength(1); j++)
            sum = array[i,j] + sum;

    if(sum < min)
    {
        min = sum;
        row = i;
    }
    }
    Console.WriteLine($"The line with the minimum sum of digits is {row + 1}");
}

int[,] myArray = CreateRandom2Array();
ShowArray2(myArray);
LineOfMin(myArray);
*/

// Задайте две матрицы. Напишите программу, которая будет находить произведение двух матриц.

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
    Console.WriteLine();
}

int[,] Multiplication(int[,] array1, int[,] array2)
{
    int[,] newArray = new int[array1.GetLength(0), array1.GetLength(1)];

    for(int i = 0; i < array1.GetLength(0); i++)
        for(int j = 0; j < array1.GetLength(1); j++)
            for(int k = 0; k < array1.GetLength(1); k++)
            {
                newArray[i,j] += array1[i,k] * array2[k,j];
            }
    return newArray;
}

Console.WriteLine("Input number of rows: ");
int m = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Input number of colums: ");
int n = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Input the min possible value: ");
int min = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Input the max possible value: ");
int max = Convert.ToInt32(Console.ReadLine());

int[,] userArray1 = CreateRandom2Array(m, n, min, max);
ShowArray2(userArray1);
int[,] userArray2 = CreateRandom2Array(m, n, min, max);
ShowArray2(userArray2);
ShowArray2(Multiplication(userArray1, userArray2));
*/

// Сформируйте трёхмерный массив из неповторяющихся двузначных чисел. Напишите программу, которая будет построчно выводить массив, добавляя индексы каждого элемента.

int[,,] CreateRandom3Array()
{
    Console.WriteLine("Input length (5): ");
    int length = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine("Input wide (4): ");
    int wide = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine("Input height (4): ");
    int height = Convert.ToInt32(Console.ReadLine());

    int[,,] newArray = new int[length, wide, height];
    int[] checkarray = new int[90];
    int count = 0;
    int temp = 9;
    int index = 0;
    
    if (length * wide * height < 90)
    {
        for(int i = 0; i < length; i++)
        {
            for(int j = 0; j < wide; j++)
            {
                for(int z = 0; z < height; z++)
                {   
                    temp = new Random().Next(10, 99);
        
                    for (int current = 0; current < 90; current++)
                    {
                        if (checkarray[current] == temp) count = 1;
                    }

                    if (count == 0) 
                    {  
                        newArray[i, j, z] = temp;
                        checkarray[index + 1] = temp;
                    }
                }   
            }
        }
    }
    return newArray;
}

void ShowArray3(int[,,] array)
{
    for(int i = 0; i < array.GetLength(0); i++)
    {
        for(int j = 0; j < array.GetLength(1); j++)
        {
            for(int k = 0; k < array.GetLength(2); k++)
                {
                    Console.Write(array[i, j, k]);
                    Console.Write($"({i}, {j}, {k}) ");
                }
            Console.WriteLine();
        }
    }
    Console.WriteLine();
}


int[,,] userArray = CreateRandom3Array();
ShowArray3(userArray);

// Напишите программу, которая заполнит спирально массив 4 на 4. 
////////////////////Задача 62. Напишите программу, которая заполнит спирально массив 4 на 4.

// Console.Write("Enter rows numbers: ");
// int rows = Convert.ToInt32(Console.ReadLine());
// Console.Write("Enter columns numbers: ");
// int columns = Convert.ToInt32(Console.ReadLine());

// int w = 1;

// int [,] array = new int [rows, columns];

// for (int y = 0; y < columns; y++)
// {
//     array [0,y] = w;
//     w++;
// }

// for (int x = 1; x < rows; x++)
// {
//     array [x, columns - 1] = w;
//     w++;
// }

// for (int y = columns - 2; y >= 0; y--)
// {
//     array [rows - 1, y] = w;
//     w++;
// }

// for (int x = rows - 2; x > 0; x--)
// {
//     array [x, 0] = w;
//     w++;
// }

// int c = 1;
// int d = 1;

// while (w < rows * columns)
// {
//     while (array [c, d + 1] == 0)
//     {
//         array [c,d] = w;
//         w++;
//         d++;
//     }

//     while (array[c + 1, d] == 0) 
//     {
//         array[c, d] = w;
//         w++;
//         c++;
//     }
 
//     while (array[c, d - 1] == 0) 
//     {
//         array[c, d] = w;
//         w++;
//         d--;
//     }
 
//     while (array[c - 1, d] == 0) 
//     {
//         array[c, d] = w;
//         w++;
//         c--;
    
//     }

//     for (int x = 0; x < rows; x++) 
//     {
//         for (int y = 0; y < columns; y++) 
//         {
//             if (array[x, y] == 0) 
//             {
//                 array[x, y] = w;
//                 w++;
//             }
//         }
//     }


//     for (int x = 0; x < rows; x++) 
//     {
//         for (int y = 0; y < columns; y++) 
//         {
//             if (array[x, y] < 10) 
//             {
//                 Console.Write(array[x, y] + ",  ");
//             }    
//             else 
//             {
//                 Console.Write(array[x, y] + ", ");
//             }
//         }  
//         Console.WriteLine("");
//     }
// }
