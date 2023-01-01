// Type 1
/*
void Method1()
{
    Console.WriteLine("Author ...");
}

Method1();
// Method; - Скобочки при вызове метода ОБЯЗАТЕЛЬНЫ!!!
*/

// Type 2
/*
void Method2(string msg)
{
    Console.WriteLine(msg);
}
Method2("Message");

void Method21(string msg, int count)
{
    int i = 0;
    while(i < count)
    {
        Console.WriteLine(msg);
        i++;
    }
    
}
Method21("Text", 4);

void Method212(string msg, int count)
{
    int i = 0;
    while(i < count)
    {
        Console.WriteLine(msg);
        i++;
    }
    
}
Method212(msg: "Text", count: 4); // Именованные аргументы можно перечислять в любом порядке.
*/

//Type 3
/*
int Method3()
{
    return DateTime.Now.Year;
}

int year = Method3();
Console.WriteLine(year);
*/

//Type 4
/*
string Method4(int count, string c)
{
    int i = 0;
    string result = String.Empty;
    
    while (i < count)
    {
        result = result + c;
        i ++;
    }
    return result;
}

string res = Method4(10, "asdfa");
Console.WriteLine(res);
*/

