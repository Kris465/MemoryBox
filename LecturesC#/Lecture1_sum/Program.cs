/*
int number1 = 3;
int number2 = 5;
Console.WriteLine(number1 + number2);
*/

/*
int number1 = 3;
int number2 = 5;
int result = number1 + number2; // We have created a new box for the sum of two numbers, especially we will need it
Console.WriteLine(result);
*/

int number1 = new Random().Next(1,10); 
Console.WriteLine(number1);
int number2 = new Random().Next(1,10);
Console.WriteLine(number2);
int result = number1 + number2;
Console.WriteLine(result);