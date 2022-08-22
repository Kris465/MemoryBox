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

