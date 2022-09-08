// Как правильно писать код. 

// Неудачные примеры:
/*
void Method(int maximum)
{
    int minimum;
    minimum = -maximum;
    while (minimum <= maximum)
    {
        Console.Write(minimum + " ");
        minimum++;
    }
}

Method(5);
*/

/*
int[] CreateArray(int N)
{
    int[] arrayA = new int[N * 2 + 1];
    for (int i = -N; i <= N; i++)
    {
        arrayA[i + N] = i;
    }
    return arrayA;
}

Console.WriteLine(CreateArray(5));
*/

/*
int Ar (int N) // задаем метод
{
    int x = -N; // первая цифра -N (задаем цикл)
    while (x <= N ) // до тех пор пока х меньше или равен N
    {
        Console.WriteLine(x); // выводим в консоль "x"
            x++; // инкремент
    }
    return x;
}

Console.WriteLine(Ar(5));
*/

/*
void Numbers(int n)
{
    int length = n + n;
    for (int i = 0; i < length + 1; i++)
    {
        

        Console.WriteLine(-n + i);
    }


}

Numbers(5);
*/

/*
string ShowNums(int N)
{
    string NumsShow = "";
    for (int i = -N; i < N; i++)
    {
        NumsShow = NumsShow + i + " ";
    }
    return NumsShow;

}

Console.WriteLine(ShowNums(5));
*/

// Удачный пример:
/*
int af = -5;
int uf = 5;
Console.WriteLine($"{af}..{uf}");

Ага, ха-ха. 
*/

// Что в коде можно улучшить?
// 1. Имена переменных. 
// 2. Имя метода.
// 3. Имена аргументов метода. 

// Для с# https://docs.microsoft.com/en-us/dotnet/standard/design-guidelines/

/*
int a = 12;
Console.WriteLine(a.GetType());
*/

using System.Linq;

var a = 12;
Console.WriteLine(a.GetType());

var data = new int[] {1, 2, 3, 4}
    .Where(e => e > 0)
    .Select(e => new {q = e, w = e + 1});
Console.WriteLine(data.GetType());