// Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка.
/*
int FindQuadrant(double x, double y)
{
    if(x > 0 && y > 0) return 1;
    if(x < 0 && y > 0) return 2;
    if(x < 0 && y < 0) return 3;
    if(x > 0 && y < 0) return 4;
    return 0;
}

Console.Write("Input x: ");
double xA = Convert.ToDouble(Console.ReadLine());
Console.Write("Input y: ");
double yA = Convert.ToDouble(Console.ReadLine());

int quadrant = FindQuadrant(xA, yA);
Console.WriteLine($"Num of quad is {quadrant}");
*/

// Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
/*
void FindXandY(int number)
{
    if(number == 1)
    Console.WriteLine("x > 0 and y > 0");
    if(number == 2)
    Console.WriteLine("x < 0 and y > 0");
    if(number == 3)
    Console.WriteLine("x < 0 and y < 0");
    if(number == 4)
    Console.WriteLine("x > 0 and y < 0");
    if(number > 4 || number < 1)
    Console.WriteLine("There isn't");
}

Console.Write("Input number: ");
int num = Convert.ToInt32(Console.ReadLine());
FindXandY(num);
*/

// Напишите программу, которая принимает на вход число (n) и выдаёт квадраты чисел от 1 до n.
/*
void Square(int number)
{
    int current = 1;
    while(current <= number)
    {
        Console.Write(current * current + " ");
        current ++;
    }
}

Console.Write("Input number: ");
int num = Convert.ToInt32(Console.ReadLine());
Square(num);
*/ 

// Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве. Math.Sqrt() 4 переменных, возвращается double
/*
double FindDistance(double x1, double y1, double x2, double y2)
{
    return Math.Sqrt((x2 - x1) * (x2 - x1) * (y2 - y1) * (y2 - y1));
}

Console.WriteLine("Enter the first dot: ");
double xA = Convert.ToDouble(Console.ReadLine());
double yA = Convert.ToDouble(Console.ReadLine());
Console.WriteLine("Enter the second dot: ");
double xB = Convert.ToDouble(Console.ReadLine());
double yB = Convert.ToDouble(Console.ReadLine());

double dist = FindDistance(xA, yA, xB, yB);
Console.WriteLine($"Distance is {dist}");
*/
