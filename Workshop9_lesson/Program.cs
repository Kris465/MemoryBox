// Задайте значение N. Напишите программу, которая выведет все натуральные числа в промежутке от 1 до N.

/*

int count = 1;

void ShowNums(int n)
{
    Console.WriteLine(count);
    count++;
    ShowNums(n);
}
*/

/*
void ShowNums(int n)
{
    if(n > 1) ShowNums(n - 1);

    Console.Write(n + " ");
}

ShowNums(5);
*/

/*
void ShowNums(int n)
{
    if(n >= 1)
    {
        Console.Write(n + " ");
        ShowNums(n - 1);
    }
    
}

ShowNums(5);
*/

/*
void ShowNums(int n)
{
    if(n > 1)
    {
        Console.Write(n + " ");
        ShowNums(n - 1);
    }

    Console.Write(n + " ");   
}

ShowNums(5);
*/

// Напишите программу, которая будет принимать на вход число и возвращать сумму его цифр.
/*
int SumOfDigits(int n)
{
    if(n > 0) return SumOfDigits(n / 10) + n % 10;
    else return 0;
}

Console.Write(SumOfDigits(5364));
*/

/*
int SumOfDigits(int n)
{
    if(n > 0) 
    {
        SumOfDigits(n / 10);
        return n % 10;
    }
    else return 0;
}

Console.Write(SumOfDigits(234235));
*/

/*
void ShowNums(int m, int n)
{
    if(n > m)
    {
        if(n > m) ShowNums(m, n - 1);
        Console.Write(n + " ");
    }
    else
    {
        if(m > n) ShowNums(m - 1, n);
        Console.Write(m + " ");
    }
}

ShowNums(20, 3);
*/ 

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

// Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
/*
int PowValue(int a, int b)
{
    if(b > 1) return PowValue(a, b - 1) * a;
    else return a;
}

Console.WriteLine(PowValue(2, 3));
*/