// 10. Напишите программу, которая принимает на вход трехзначное число и на выходе показывает вторую цифру этого числа.
/*
int SecondDigit(int number)
{
    int digit = number / 10;
    int newdigit = digit % 10;
    return newdigit;
}

Console.Write("Input your number: ");
int inputnum = Convert.ToInt32(Console.ReadLine());
int outputdigit = SecondDigit(inputnum);
Console.WriteLine($"The second digit in number is {outputdigit}");
*/

// 13. Напишите программу, которая вываодит третью цифру заданного числа или сообщает, что третьей цифры нет. 
/*
int ThirdDigit(int number)
{
    if(number >= 100)
    {
        int current = number;
        int output = 0;
        while(current > 1000)
        {
            current /= 10;
    }
        return output = current % 10;
    }
    else 
    {
        return -1;
    }
}

Console.Write("Input your number: ");
int inputnum = Convert.ToInt32(Console.ReadLine());
Console.WriteLine(ThirdDigit(inputnum));
*/

/*
void ThirdDigit(int number)
{
    if(number >= 100 ^ number <= -100)
    {
        int current = number;
        int output = 0;
        while(current > 1000 ^ current < -1000)
        {
            current /= 10;
        }   
        output = current % 10; 
        if (output < 0) output = output * (-1);
        Console.WriteLine($".... {output}");
    }
    else 
    {
        Console.WriteLine("....");
    }
}

Console.Write("Input your number: ");
int inputnum = Convert.ToInt32(Console.ReadLine());
ThirdDigit(inputnum);
*/

/*
int ThirdDigit(int number)
{
    if(number >= 100)
    {
        int current = number;
        int output = 0;
        while(current > 1000)
        {
            current /= 10;
        }
        return output = current % 10;
    }
    else 
    {
        return -1;
    }
}

Console.Write("Input your number: ");
int inputnum = Convert.ToInt32(Console.ReadLine());
Console.WriteLine(ThirdDigit(inputnum));
*/

// 15. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

void DayOfWeek(int number)
{
    if(number < 6)
    {
        Console.WriteLine("Yes");
    }
    else
    {
        Console.WriteLine("No");
    }
}

Console.Write("Input your number: ");
int inputnum = Convert.ToInt32(Console.ReadLine());
DayOfWeek(inputnum);