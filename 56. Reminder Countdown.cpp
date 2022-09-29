//Name: Alysa Liann Vega
//Email: alysa.vega72@myhunter.cuny.edu
//Date: November 23, 2021
//This C++ program counts down to a reminder

#include <iostream>
using namespace std;

int main()
{
    int num;
    string word;
    cout << "Please enter a number: ";
    cin >> num;
    cout << "Please type a word: ";
    cin >> word;
    for (num < num+1; num > 0; num--)
    {
        cout << num << "," << endl;
    }
    cout << "Time for " << word << "!";
    return 0;
}
