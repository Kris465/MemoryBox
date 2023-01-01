// 25. Напишите цикл, который принимает на вход два числа (A и B) и возводит число A в натуральную степень B.
/*
int DegreeOfNum(int number, int degree)
{
    int multi = number;

    for (int current = 1; current < degree; current ++)
        multi *= number;
    
    return multi;
}

Console.WriteLine("Input your number: ");
int num = Convert.ToInt32(Console.ReadLine());

Console.WriteLine("Input the degree of the number: ");
int deg = Convert.ToInt32(Console.ReadLine());

Console.WriteLine(DegreeOfNum(num, deg));
*/

// 27. Напишите программу, которая принимает на вход число и выдаёт сумму цифр в числе.
/*
int SumOfDigits(int number)
{
    int current = number;
    int digits = 0;
    int sumdigit = 0;
    while (current > 0)
    {
        sumdigit = (current % 10) + sumdigit;
        current = current / 10;
        digits ++;
    }
    return sumdigit;
}

Console.Write("Input your number: ");
int num = Convert.ToInt32(Console.ReadLine());

Console.WriteLine(SumOfDigits(num));
*/

// 29. Напишите программу, которая задаёт массив из 8 элементов и выводит их на экран.
/*
int[] AskArray(int size, int[] num)
{
    int[] newArray = new int[size];

    for(int i = 0; i < size; i++) 
        newArray[i] = Convert.ToInt32(Console.ReadLine());

    return newArray;
}

void ShowArray(int[] array)
{
    for(int i = 0; i < array.Length; i ++)
        Console.Write(array[i] + " ");

    Console.WriteLine();    
}

Console.WriteLine("Input the size of your array: ");
int askedsize = Convert.ToInt32(Console.ReadLine());

Console.Write("Input numbers for your array: ");
int[] num = Convert.ToInt32(Console.ReadLine());
ShowArray(AskArray(askedsize, num));
*/

/* // Кусок некой херни
void Main(string[] args)
    {
        Console.WriteLine("Введите размерность массива:");
        int i, n = Convert.ToInt32(Console.ReadLine());
        int[] mas = new int[n];
        Console.WriteLine("Введите массив:");
        string[] str = Console.ReadLine().Split(new char[] { ' ', '\n', '\t' }, StringSplitOptions.RemoveEmptyEntries);
        for (i = 0; i < (n < str.Length ? n : str.Length); ++i)
            mas[i] = Convert.ToInt32(str[i]);
        Console.WriteLine("Введенный массив:");
        for (i = 0; i < n; ++i)
            Console.Write("{0} ", mas[i]);
        Console.ReadLine();
    }

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

ShowArray(CreateRandomArray(25, 0, 9));
*/
/* Моя очередная гениальная хуйня!!! ААААААААААААААААААААААА!

void AskedArray (int size, string[] array)
{
    Console.WriteLine("Input the size of your array: ");
    int i = 0;
    int num = Convert.ToInt32(Console.ReadLine());
    int[] arr = new int[size];
    Console.Write("Input your array: ");
    string[] str = Console.ReadLine();
    for (i = 0; i < size)
}
*/

int[] AskedArray()
{
    Console.WriteLine("Input the size of your array: ");
    int size = Convert.ToInt32(Console.ReadLine());

    int[] newArray = new int[size];

    Console.WriteLine($"Input please {size} numbers: ");
    for(int i = 0; i < size; i++)
    {
        Console.Write($"Input number {i + 1}: ");
        newArray[i] = Convert.ToInt32(Console.ReadLine());
    }
    return newArray;
}

void ShowArray(int[] array)
{
    for(int i = 0; i < array.Length; i ++)
    {
        Console.Write(array[i] + " ");
    }
    Console.WriteLine();    
}

ShowArray(AskedArray());
