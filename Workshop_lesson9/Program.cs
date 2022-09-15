// Задайте значение N. Напишите программу, которая выведет все натуральные числа в промежутке от 1 до N.
/*
void ShowNums(int n)
{
    if(n > 1) ShowNums(n-1);

    Console.Write(n + " ");
}

ShowNums(5);
*/
// Условие работы? 

// Напишите программу, которая будет принимать на вход число и возвращать сумму его цифр.
/*
int SumOfDigits(int n)
{
    if (n > 0) return SumOfDigits(n / 10) + n % 10;
    else return 0;
}

Console.Write(SumOfDigits(5364));

// 5364
*/

// Задайте значения M и N. Напишите программу, которая выведет все натуральные числа в промежутке от M до N.
/*
void ShowNums(int m, int n)
{
    if(m > n) ShowNums(m, n-1);
    Console.Write(n + " ");
}

ShowNums(29, 1);
*/
// Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии. 

int Degree(int a, int b)
{
    if (b > 1) return Degree(a, b - 1)*a;
    else return a;
}

Console.WriteLine(Degree(2, 3));