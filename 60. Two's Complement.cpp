//Name: Alysa Liann Vega
//Email: alysa.vega72@myhunter.cuny.edu
//Date: November 23, 2021
//This C++ program converts a user inputted number to a binary number

#include <iostream>
using namespace std;

int main()
{
    int n,x;
    cout << "Enter a whole number between -31 and 31: ";
    cin >> n;
    if (n < 0)
    {
        cout << "1";
        x = 32 + n;
    }
    else
    {
        cout << "0";
        x = n;
    }
    int b = 16;
    while (b > 0.5)
    {
        if (x >= b)
        {
            cout << "1";
        }
        else
        {
            cout << "0";
        }
        x = x % b;
        b = b / 2;
    }
    cout << endl;
    return 0;    
}