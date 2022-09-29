//Name: Alysa Liann Vega
//Email: alysa.vega72@myhunter.cuny.edu
//Date: November 23, 2021
//This C++ program converts cryptocurrency to USD

#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	float crypto,Bcon,Econ,Dcon;
	cout << "Enter amount in cryptocurrency: ";
	cin >> crypto;
	Bcon = crypto * 31901.19;
	Econ = crypto * 1901.54;
	Dcon = crypto * 0.179733;
	cout << fixed << setprecision(2);
	cout << crypto << " BTC in USD: $" << Bcon << endl << crypto << " ETH in USD: $" << Econ << endl << crypto << " DOGE in USD: $" << Dcon;
	return 0;
}