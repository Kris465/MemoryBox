// Задайте двумерный массив. Напишите программу, которая поменяет местами первую и последнюю строку массива.

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
}

void ChangeRows(int[,] array, int row1, int row2)
{
    if(row1 >= 0 && row1 < array.GetLength(0) && row2 >= 0 && row2 < array.GetLength(0) && row1 != row2)
        for (int j = 0; j < array.GetLength(1); j++)
        {
            int temp = array[row1, j];
            array[row1, j] = array[row2, j];
            array[row2, j] = temp;
        }
}


int[,] myArray = CreateRandom2Array();
ShowArray2(myArray);
ChangeRows(myArray, 0, 8);
ShowArray2(myArray);
*/

// Задайте двумерный массив. Напишите программу, которая заменяет строки на столбцы. В случае, если это невозможно, программа должна вывести сообщение для пользователя. Главная диагональ, меняем местами итые и житые. На вход массив, метод может быть войдовским. Проверить, квадратный массив или нет? Сначала проверить. 
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

void ReverseArray(int[,] array)
{
    for (int i = 0; i < array.GetLength(0) - 1; i++)
    {
        for (int j = i + 1; j < array.GetLength(1); j++)
        {
            int temp = array[i, j];
            array[i, j] = array[j, i];
            array[j, i] = temp;
        }
    }
}

int[,] array = CreateRandom2Array();
ShowArray2(array);
ReverseArray(array);
ShowArray2(array);
*/

// Из двумерного массива целых чисел удалить строку и столбец, на пересечении которых расположен наименьший элемент. Найти индекс минимального элемента. Выделить новый массив и перезаписать туда этот массив без строк. Или заполнить в строку или столбец нули. Истино минимальный - первый. 
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
}

void DeleteArray(int[,] array)
{
    int iMin = 0;
    int jMin = 0;

    for(int i = 0; i < array.GetLength(0); i++)
        for(int j = 0; j < array.GetLength(1); j++)
        {
            if(array[i, j] < array[iMin, jMin])
                {
                    iMin = i;
                    jMin = j;
                } 
        }

    for(int i = 0; i < array.GetLength(0); i++)
        for(int j = 0; j < array.GetLength(1); j++)
        {
            if((i == iMin) || (j == jMin))
                {
                    array[i, j] = 0;
                }        
        } 
}

int[,] array = CreateRandom2Array();
ShowArray2(array);
DeleteArray(array);
ShowArray2(array);
*/

// Написать программу поэлементного копирования массива. Новый массив с теме же элементами, что и старый. 

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
}

int[,] CreateCopyFirstArray(int[,] array)
{
     int[,] newArray = new int[array.GetLength(0), array.GetLength(1)];
     for(int i = 0; i < array.GetLength(0); i++)
         for(int j = 0; j < array.GetLength(1); j++)
         {
             newArray[i, j] = array[i,j];
         }
     return newArray;
}

int[,] array = CreateRandom2Array();
ShowArray2(array);
Console.WriteLine();
int[,] newArray = CreateCopyFirstArray(array);
ShowArray2(newArray);