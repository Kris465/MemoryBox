/*Console.Write("Input number: ");
int number = Convert.ToInt32(Console.ReadLine());
int square = number * number;
Console.WriteLine("The square is " + square);
*/

/*Console.Write("Input number 1: ");
Console.Write("Input number 2: ");

int number1 = Convert.ToInt32(Console.ReadLine());
int number2 = Convert.ToInt32(Console.ReadLine());

int square = number2 * number2;

if (number1 == square)
{
    Console.Write("The first number is a square of second number");
}
else 
{
    Console.Write("The second number isnt a square");
}
*/

Console.Write("Input number: ");
int number = Convert.ToInt32(Console.ReadLine());

int current = number * (-1);

while(current <= number)
{
    Console.Write(current + " ");
    current ++;
    
}

