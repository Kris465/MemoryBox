// Напишите программу, которая перевернёт одномерный массив (последний элемент будет на первом месте, а первый - на последнем и т.д.)
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

int[] ReverseArray(int[] array)
{
    for (int i = 0; i < array.Length / 2; i++)
    {
        int temp = array[i];
        array[i] = array[array.Length - 1 - i]; // i - двигаемся из конца в начало
        array[array.Length- 1 - i] = temp;
    }
    return array;
}


Console.Write("Input size of array: ");
int size = Convert.ToInt32(Console.ReadLine());
Console.Write("Input min possible value: ");
int min = Convert.ToInt32(Console.ReadLine());
Console.Write("Input max possible value: ");
int max = Convert.ToInt32(Console.ReadLine());

int[] myArray = CreateRandomArray(size, min, max);
ShowArray(myArray);
myArray = ReverseArray(myArray);
Console.WriteLine(myArray);
*/

// Скорость выполнения программы, сколько памяти занимает программа, читабельность кода программы

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

int[] ReverseArray(int[] array)
{
    for (int i = 0, j = array.Length - 1; i < j; i++, j--)
    {
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
    return array;
}


Console.Write("Input size of array: ");
int size = Convert.ToInt32(Console.ReadLine());
Console.Write("Input min possible value: ");
int min = Convert.ToInt32(Console.ReadLine());
Console.Write("Input max possible value: ");
int max = Convert.ToInt32(Console.ReadLine());

int[] myArray = CreateRandomArray(size, min, max);
ShowArray(myArray);
*/

// Напишите программу, которая принимает на вход три числа и проверяет, может ли существовать треугольник с сторонами такой длины. a < b + c Берет на вход три числа, возвращает bool
/*
bool Triangle(int num1, int num2, int num3)
{
    if (num1 < num2 + num3 && num2 < num1 + num3 && num3 < num1 + num2) return true;
    else return false;
}

Console.WriteLine("... ");
int first = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("... ");
int second = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("... ");
int third = Convert.ToInt32(Console.ReadLine());
Console.WriteLine(Triangle(first, second, third));

*/


// Не используя рекурсию, выведите первые N чисел Фибоначчи. Первые два числа Фибоначчи: a и b. Каждое следующее - сумма двух предыдущих. F(n) = F(n-1) + F(n-2)
/*
int[] Fibonacci(int size, int first, int second)
{
    int[] newarray = new int[size];
    newarray[0] = first;
    newarray[1] = second;
    for (int i = 2; i < size; i++)
    {
        newarray[i] = newarray[i - 1] + newarray[i - 2];
    }
    return newarray;
}

void ShowArray(int[] array)
{
    for(int i = 0; i < array.Length; i ++)
        Console.Write(array[i] + " ");

    Console.WriteLine();    
}

ShowArray(Fibonacci(10, 0, 1));
*/

// Напишите программу, которая будет преобразовывать десятичное число в двоичное. Поэтапно делим на два, берем остаток от деления и полученное число делим на два. Пока не останется 1. Записываем остатки от деления в обратном порядке. Приклеивать строку слева. 

string Number(int number)
{
    string show = string.Empty;
    while (number > 0)
    {
        show = (number % 2) + show;
        number /= 2;
    }
    return show;
}

Console.WriteLine(Number(100));


