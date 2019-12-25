#include <iostream>
#include <stdio.h>
#include <iomanip>
#include <cmath>

using namespace std;
using std::setw;

int phi(unsigned int n) {
	unsigned int i;
	double result = n;

	for (i = 2; i <= sqrt(n); i++) {
		if (n % i == 0) {
			while (n % i == 0) {
				n = n/i;
			}
			result = result * (1.0 - (1.0/ i));
		}
	}

	if (n>1) {
		result = result * (1.0 - (1.0/ n));
	}

	return result;
}

int phi_divided_n(double result, unsigned int n) {
	double ans;

	ans = result / n;

	if (n <= pow(2,15)) {
		cout.precision(5);
		cout << "phi(n)/n" << setw(13) << "= " << ans << endl;
	}
}

int main() {
unsigned int n;
	cin >> n;
	cout << "n" << setw(20) << "= " << n << endl;
	double result;
	result = phi(n);
	cout << "phi(n)" << setw(15) << "= ";
	cout << fixed;
	cout.precision(0);
	cout << result << endl;
	phi_divided_n(result, n);

	/*

	unsigned int n;
	cout << "Enter a number: ";
	cin >> n;
	cout << "n" << setw(20) << "= " << n << endl;
	double result;
	result = phi(n);
	cout << "phi(n)" << setw(15) << "= ";
	cout << fixed;
	cout.precision(0);
	cout << result << endl;
	phi_divided_n(result, n);

	while (n != 1) {
		cout << "Enter a number: ";
		cin >> n;
		cout << "n" << setw(20) << "= " << n << endl;
		result = phi(n);
		cout << "phi(n)" << setw(15) << "= ";
		cout << fixed;
		cout.precision(0);
		cout << result << endl;
		phi_divided_n(result, n);
	}
*/
	return 0;
}