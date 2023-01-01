int Max(int arg1, int arg2, int arg3)
{
    int result = arg1;
    if(arg2 > result) result = arg2;
    if(arg3 > result) result = arg3;
    return result;
}

int[] array = {11, 21, 31, 41, 15, 61, 17, 18, 19}; // Индексы с нуля!!!

/*
array[0] = 12; // Как обратиться к массиву и записать в него значение
Console.WriteLine(array[0]); // Как обратиться к массиву и получить значение соответсвующего элемента по указанному индексу
*/

int max = Max(
    Max(array[0], array[1], array[2]),
    Max(array[3], array[4], array[5]),
    Max(array[6], array[7], array[8])
);
Console.WriteLine(max);