using System;

class Program {
    static void Main() {
        Console.Write("Input the first number: ");
        double num1 = Convert.ToDouble(Console.ReadLine());
        Console.Write("Input the second number: ");
        double num2 = Convert.ToDouble(Console.ReadLine());
        Console.WriteLine($"Sumup {num1 + num2}");
    }
}