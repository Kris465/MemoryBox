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

