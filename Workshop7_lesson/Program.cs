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