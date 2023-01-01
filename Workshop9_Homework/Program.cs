// Задайте значения M и N. Напишите программу, которая выведет все натуральные числа в промежутке от M до N.
/*
void ShowNums(int m, int n)
{
    if(n > m) ShowNums(m, n - 1);

    Console.Write($"{n}, ");
}

Console.WriteLine("Input the first numer: ");
int min = Convert.ToInt32(Console.ReadLine()); 
Console.WriteLine("Input the first numer: ");
int num = Convert.ToInt32(Console.ReadLine()); 
ShowNums(min, num);
*/
//  Задайте значения M и N. Напишите программу, которая найдёт сумму натуральных элементов в промежутке от M до N.
/*
int SumOfDigits(int m, int n)
{
    if(n > m) return SumOfDigits(m, n - 1) + n;
    else return m;
}

Console.WriteLine("Input the first numer: ");
int min = Convert.ToInt32(Console.ReadLine()); 
Console.WriteLine("Input the first numer: ");
int num = Convert.ToInt32(Console.ReadLine()); 
Console.Write(SumOfDigits(min, num));
*/

//  Напишите программу вычисления функции Аккермана с помощью рекурсии. Даны два неотрицательных числа m и n.

int FuncAkkerman(int n, int m)
{
    if(n == 0) return m + 1;
    else if(n > 0 && m == 0) return FuncAkkerman(n - 1, 1);
    else if(n > 0 && m > 0) return FuncAkkerman(n - 1, FuncAkkerman(n, m - 1));
    else return 0;
}

Console.WriteLine("Input the first numer: ");
int first = Convert.ToInt32(Console.ReadLine()); 
Console.WriteLine("Input the first numer: ");
int second = Convert.ToInt32(Console.ReadLine()); 
Console.Write(FuncAkkerman(second, first));