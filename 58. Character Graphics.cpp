//Name: Alysa Liann Vega
//Email: alysa.vega72@myhunter.cuny.edu
//Date: November 23, 2021
//This C++ program creates a trapezoid using user input

#include <iostream>
using namespace std;

int main()
{
    int n;
    char c;
    cout << "Enter a number: ";
    cin >> n;
    cout << "Enter a character: ";
    cin >> c;
    int j = n;
    int nn = 2 * n;
    for (int i = 0; i < n; i++)
    {
            for(int j = 0; j <= i; j++)
            {
                cout << c;
            }
        cout << endl;
    }
    for (int i = 0; i < n; i++)
    {
        for(int j = n; j < n+n; j++)
            {
                cout << c;
            }
        cout << endl;
    }
    return 0;
}