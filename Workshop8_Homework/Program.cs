﻿// Задайте двумерный массив. Напишите программу, которая упорядочит по убыванию элементы каждой строки двумерного массива.

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


// Задайте прямоугольный двумерный массив. Напишите программу, которая будет находить строку с наименьшей суммой элементов.

// Задайте две матрицы. Напишите программу, которая будет находить произведение двух матриц.

// Сформируйте трёхмерный массив из неповторяющихся двузначных чисел. Напишите программу, которая будет построчно выводить массив, добавляя индексы каждого элемента.

// Напишите программу, которая заполнит спирально массив 4 на 4. 
