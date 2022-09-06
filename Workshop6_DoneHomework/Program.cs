// Пользователь вводит с клавиатуры M чисел. Посчитайте, сколько чисел больше 0 ввёл пользователь. Без применения массива. 

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

