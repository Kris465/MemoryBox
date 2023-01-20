Console.WriteLine("Input the amount of element in your array: ");
int size = Convert.ToInt32(Console.ReadLine()); 
const int line = 4;

string[] CreateArray()
{
    string[] newArray = new string[size];

    for(int i = 0; i < size; i++)
    {
        Console.Write($"Input element {i + 1}: ");
        newArray[i] = Console.ReadLine();
    }
    return newArray;
}

void ShowArray(string[] array)
{
    for(int i = 0; i < size; i++) Console.Write($" {array[i]} ");
}

string[] SecondArray(string[] array)
{
    string[] newArray = new string[array.Length];
    for(int i = 0; i < size; i++)
    {
        if(array[i].Length < line)
        {
            newArray[i] = array[i];
        }
    }
    return newArray;
}

string[] MyArray = CreateArray();
Console.WriteLine("NewArray is: ");
ShowArray(MyArray);
Console.WriteLine();
Console.WriteLine("Second array is: ");
ShowArray(SecondArray(MyArray));