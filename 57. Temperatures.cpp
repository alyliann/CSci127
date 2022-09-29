//Name: Alysa Liann Vega
//Email: alysa.vega72@myhunter.cuny.edu
//Date: November 23, 2021
//This C++ program prints a statement about the temperature

#include <iostream>
using namespace std;

int main()
{
    int temp;
    cout << "Enter the temperature: ";
    cin >> temp;
    if (temp <= 32)
    {
        cout << "It's freezing!";
    }
    if (temp < 68 and temp > 32)
    {
        cout << "It's cold!";
    }
    if (temp >= 68 and temp < 73)
    {
        cout << "It's warm!";
    }
    if (temp >= 73)
    {
        cout << "It's hot!";
    }
    return 0;
}