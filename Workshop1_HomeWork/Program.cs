// Ex. 2 "Напишите программу, которая на вход принимает два числа и выдает, какое число большее, а какое меньшее."

/* 
Console.Write("Input the first number: ");
int number1 = Convert.ToInt32(Console.ReadLine());

Console.Write("Input the second number: ");
int number2 = Convert.ToInt32(Console.ReadLine());


if(number1 > number2)
{
    Console.WriteLine(number1 + " is more than " + number2);
}
else
{
    Console.WriteLine(number2 + " is more than " + number1);
}
*/


// Ex. 4 "Напишите программу, которая принимает на вход три числа и выдает максимальное из этих чисел."

/*
Console.Write("Input the first number: ");
int number1 = Convert.ToInt32(Console.ReadLine());

Console.Write("Input the second number: ");
int number2 = Convert.ToInt32(Console.ReadLine());

Console.Write("Input the third number: ");
int number3 = Convert.ToInt32(Console.ReadLine());

if(number1 > number2)
{
    if(number1 > number3)
    {
        Console.WriteLine("Maximum number is " + number1);
    }
    else
    {
        Console.WriteLine("Maximum number is " + number3);
    }
}
else
{
    if(number2 > number3)
    {
        Console.WriteLine("Maximum number is " + number2);
    }
    else
    {
        Console.WriteLine("Maximum number is " + number3);
    }
}
*/

// Ex. 6 "Напишите программу, которая на вход принимает число и выдает является ли число четным (делится ли оно на два без остатка)."

/*
Console.Write("Input your number: ");
int number = Convert.ToInt32(Console.ReadLine());

if (number % 2 == 0)
{
    Console.WriteLine("You have input the even number.");
}
else
{
    Console.WriteLine("You have input the odd number.");
}
*/

// Ex. 8 "Напишите программу, которая на вход принимает число (N), a на выходе показывает все четные числа от 1 до N."

/*
Console.Write("Input your number: ");
int number = Convert.ToInt32(Console.ReadLine());

int current = 1;

while(current <= number)
{
    if(current % 2 == 0)
    {
        Console.Write(current);
    }
    else
    {
        Console.Write(" ");
    }
    current = current + 1;
}
*/