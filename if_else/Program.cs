/*
Console.Write("Input user's name: ");
string username = Console.ReadLine();

if(username == "Masha")
{
    Console.WriteLine("Hooray, this is Masha!");
}
else 
{
    Console.Write("Hello, " + username + "!");
}
*/

Console.Write("Input user's name: ");
string username = Console.ReadLine();

if(username.ToLower() == "masha")
{
    Console.WriteLine("Hooray, this is Masha!");
}
else 
{
    Console.Write("Hello, " + username + "!");
}