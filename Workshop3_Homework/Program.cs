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
     while(check < length / 2)
     {
          if(number / firstnum == cutnum % 10)
          {
               Console.WriteLine("Your number isn't a palindrome");
          }
          firstnum = firstnum - 1;
          cutnum = cutnum / 10;
          check = check + 1;    
     } 
}

Console.Write("Input yout number: ");
int num = Convert.ToInt32(Console.ReadLine());
Palindrome(num);

// 21. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 3D пространстве.

// 23. Напишите программу, которая принимает на вход число (N) и выдаёт таблицу кубов чисел от 1 до N.

