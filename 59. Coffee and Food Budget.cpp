//Name: Alysa Liann Vega
//Email: alysa.vega72@myhunter.cuny.edu
//Date: November 23, 2021
//This C++ program calculates user coffee budget

#include <iostream>
using namespace std;

int main()
{
    float budg,spend;
    cout << "Enter your monthly budget for food and coffee: ";
    cin >> budg;
    cout << "How much are you spending in a week for coffee: ";
    cin >> spend;
    float w1 = budg - spend;
    float w2 = budg - (spend * 2);
    float w3 = budg - (spend * 3);
    float w4 = budg - (spend * 4);
    cout << "Budget left after week 1   " << w1 << endl << "Budget left after week 2   " << w2 << endl << "Budget left after week 3   " << w3 << endl << "Budget left after week 4   " << w4;
    return 0;    
}