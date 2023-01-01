// Пользователь вводит с клавиатуры M чисел. Посчитайте, сколько чисел больше 0 ввёл пользователь. Без применения массива. 
/*
void CountNum(string num)
{   
    int sum = 0;
    int number = Convert.ToInt32(num);

    if (number is int) 
    {
        if (number > 0) 
        {
            Console.WriteLine("Your number, please: ");
            sum += number;
            CountNum(Console.ReadLine());
        }
        else 
        {
            Console.WriteLine("Number, please: ");
            CountNum(Console.ReadLine());
        }
    }
    else  Console.WriteLine($" .{sum}. ");
}

Console.WriteLine("Hello! I'll count all your numbers what are positive. When you get tired, write something else.");
string number = Console.ReadLine();
CountNum(number);
*/
/*
void CheckNum (string num)
{
    try
    {
        int number = Convert.ToInt32(Console.ReadLine());
        checked(number is int);
    }
    catch (OverflowException ex)
    {
        Console.WriteLine("Thank you");
    }
}

CheckNum(Console.ReadLine());
*/

/*
void Fuck (string num)
{
    int sum = 0;
    var number = Convert.ToInt32(Console.ReadLine());
    if (number.GetType is int)
    {
        sum += num;
        Console.WriteLine("....");
    }
    else Console.WriteLine("Thank you");
}

Fuck(Console.ReadLine());
*/

/*
void Something(string num)
{
    var number = num;
    if (number.GetType is int)
    {
        Console.WriteLine("...");
    }
    else Console.WriteLine("!!!!");
}

Something(Console.ReadLine());
*/

/*
void CheckNum (string num)
{
    int num = 0;
    while (num != "stop")
    {
        int number = Convert.ToInt32(num);
        if (number > 0)  
        {
            sum += number;
            Console.WriteLine("Input your number: ");
            string curnum = Console.ReadLine();
            CheckNum(curnum);
        }
        else
        {
            Console.WriteLine("Please, input next number: ");
            string curnum = Console.ReadLine();
            CheckNum(curnum);
        }
    }
    Console.WriteLine($"Thank you. The result is {sum}.");
}

Console.WriteLine("Hello! I'll count all positive numbers that you input. When you get tired just write 'stop': ");
string somenumber = Console.ReadLine();
CheckNum(somenumber);
*/

/*
bool CheckNum (string word)
{
    if (word = Convert.ToInt32() is int) return true;
    else return false;
}

Console.WriteLine(CheckNum(Console.ReadLine()));
*/
/*
int StopWord(string word)
{
    var number = word;
    while(word != 'stop')
    {
        number = Convert.ToInt32();
        return number;
    }
    Console.WriteLine("Thank you!");
}

void Sumup(int num)
{

}
*/
/*
int StopWord(string word)
{
    while (word != "stop")
    {
        int number = Convert.ToInt32(word);
        SumUp(number);  
    }
    return -1;
}

void SumUp(int numb)
{
    int sum = numb;
    if (numb > 0)
    {    
        sum += numb;
        SumUp(sum);
    }
    if (numb == -1) Console.WriteLine($",,,{sum},, ");
}

Console.WriteLine(".....");
string userWord = Console.ReadLine();
StopWord(userWord);
*/

/*
void SumUp(int number, string stop)
{
    var arg = number;AAAAAAAAAAAAA
}
*/
/////////////// БОЖЕСТВЕННАЯ ХРЕНЬ ГОТОВА!!!!
/*
int sum = 0;

void SumUp(int number)
{
    if (number != 333)
    {
        Console.WriteLine("Input your number. If you want to leave, press 333: ");
            if (number > 0) 
            {
                sum += number;
                Console.WriteLine($"You sum is {sum}.");
            }
        int num = Convert.ToInt32(Console.ReadLine());
        SumUp(num);
        
    }
    else Console.WriteLine($"Thank you!");
}

Console.WriteLine("Hello! I'll count positive numbers! If you want to leave, press 333: ");
int usernum = Convert.ToInt32(Console.ReadLine());

SumUp(usernum);
*/

/*
int amount = 0;

void SumUp(int number)
{
    if (number != 333)
    {
        Console.WriteLine("Input your number. If you want to leave, press 333: ");
            if (number > 0) 
            {
                amount++;
                Console.WriteLine($"You input {amount} positive numbers.");
            }
        int num = Convert.ToInt32(Console.ReadLine());
        SumUp(num);
        
    }
    else Console.WriteLine($"Thank you! You input {amount + 1} positive numbers!");
}

Console.WriteLine("Hello! I'll count positive numbers! If you want to leave, press 333: ");
int usernum = Convert.ToInt32(Console.ReadLine());

SumUp(usernum);
*/

// Напишите программу, которая найдёт точку пересечения двух прямых, заданных уравнениями y = k1 * x + b1, y = k2 * x + b2; значения b1, k1, b2 и k2 задаются пользователем.

/*
void Common(double b1, double k1, double b2, double k2)
{
    if (k2 - k1 != 0)
    {
        double x = (b1 - b2) / (k2 - k1);
        double y = (k2 * b1 - k1 * b2) / (k2 - k1);
        Console.WriteLine($"Cross point is {x} in x and {y} in y");
    }
    else Console.WriteLine("Sorry, these lines don't have the same point.");
}

Console.WriteLine("Input b1, k1, b2, k2 for lines in y = k1 * x + b1, y = k2 * x + b2; I'll say the coordinate for their joint point: ");
int num1 = Convert.ToInt32(Console.ReadLine());
int number1 = Convert.ToInt32(Console.ReadLine());
int num2 = Convert.ToInt32(Console.ReadLine());
int number2 = Convert.ToInt32(Console.ReadLine());
Common(num1, number1, num2, number2);
*/