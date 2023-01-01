// 19. Напишите программу, которая принимает на вход пятизначное число и проверяет, является ли оно палиндромом.
/*
void Length(int number)
{
   int length = 1;
   int removingnum = number;
   while(removingnum > 9)
   {
        removingnum = removingnum / 10;
        length = length + 1;
   }
   Console.WriteLine(length);
}
*/
/*
void Palindrome(int length)
{
     int LengthOfNum(int number)
     {
          int length = 1;
          int removingnum = number;
          while(removingnum > 9)
          {
               removingnum = removingnum / 10;
               length = length + 1;
          }
     return length;
     }

    int check = 0;
    double firstnum = Math.Pow(10, length);
    int cutnum = number;
   while(check < length / 2);
   {
        if(number / firstnum != cutnum % 10)
        {
            Console.WriteLine("Your number isn't a palindrome");
        }
        firstnum = firstnum - 1;
        cutnum = cutnum / 10;
        check = check + 1;
   }
   Console.WriteLine("Your number is a palindrome");
}

Console.Write("Input yout number: ");
int num = Convert.ToInt32(Console.ReadLine());
Palindrome(num);
*/

/*
void Palindrome(int number)
{
   int length = 1;
   int removingnum = number;
   if(1 > 0)
   {
     while(removingnum > 9)
     {
          removingnum = removingnum / 10;
          length = length + 1;
     }
     Console.WriteLine(length);
   }
   if(1 > 0)
   {
     int check = 0;
     double firstnum = Math.Pow(10, length);
     int cutnum = number;
     while(check < length / 2);
     {
          if(number / firstnum != cutnum % 10)
          {
               Console.WriteLine("Your number isn't a palindrome");
          }
          firstnum = firstnum - 1;
          cutnum = cutnum / 10;
          check = check + 1;
     }
     Console.WriteLine("Your number is a palindrome");
   }
}

Console.Write("Input yout number: ");
int num = Convert.ToInt32(Console.ReadLine());
Palindrome(num);
*/

/*
void Palindrome(int number)
{
     int length = 1;
     int removingnum = number;

     while(removingnum > 9)
     {
          removingnum = removingnum / 10;
          length = length + 1;
     }
     Console.WriteLine(length);
   
     int check = 0;
     double firstnum = Math.Pow(10, length);
     int cutnum = number;
     length = Convert.ToInt32(length);
     firstnum = Convert.ToInt32(firstnum);
     while(check < length / 2)
     {
          while(number / firstnum == cutnum % 10)
          {
               Console.WriteLine("Your number is a palindrome");
               firstnum = firstnum - 1;
               cutnum = cutnum / 10;
          }
          check = check + 1;
          break;
     } 
}

Console.Write("Input yout number: ");
int num = Convert.ToInt32(Console.ReadLine());
Palindrome(num);
*/

/*
void Palindrome(int number)
{
     int inverse = 0;
     int newnum = number;
     while(number > 0)
     {
          int remind = number % 10;
          inverse = inverse * 10 + remind;
          number = number / 10;
     }

     if(newnum == inverse) Console.WriteLine($"Your number is a palindrome {inverse}");
     else Console.WriteLine($"Your number isn't a palindrome {inverse}");
}

Console.Write("Input yout number: ");
int num = Convert.ToInt32(Console.ReadLine());
Palindrome(num);
*/

// 21. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 3D пространстве.

/*
double FindDistance(double x1, double y1, double z1, double x2, double y2, double z2)
{
    return Math.Sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1) + (z2-z1) * (z2-z1));
}

Console.WriteLine("Enter the first dot (x, y, z) on their own lines: ");
double xA = Convert.ToDouble(Console.ReadLine());
double yA = Convert.ToDouble(Console.ReadLine());
double zA = Convert.ToDouble(Console.ReadLine());

Console.WriteLine("Enter the second dot (x, y, z) on their own lines: ");
double xB = Convert.ToDouble(Console.ReadLine());
double yB = Convert.ToDouble(Console.ReadLine());
double zB = Convert.ToDouble(Console.ReadLine());

double dist = FindDistance(xA, yA, zA, xB, yB, zB);
Console.WriteLine($"Distance is {dist}");
*/

// 23. Напишите программу, которая принимает на вход число (N) и выдаёт таблицу кубов чисел от 1 до N.
/*
void Cube(int number)
{
    int current = 1;
    while(current <= number)
    {
        Console.Write(Math.Pow(current, 3) + " ");
        current ++;
    }
}

Console.Write("Input number: ");
int num = Convert.ToInt32(Console.ReadLine());
Cube(num);
*/