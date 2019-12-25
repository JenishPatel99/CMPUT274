#include <iostream>
using namespace std;

int main() {
    // I've heard that climbing is a good workout for your legs.
    // But I haven't moved from my chair in years, so I might not be the best person to ask.
    // Good luck with the problem! The term is almost over! :)

	// Read in the input
	int n;
	cin >> n;
	long arr[n];
	int prev = -1000000;
	int storage[n];
	int counter = 0;

	for  (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (j > i) {
				if (arr[i] < arr[j]) {
					if (prev < arr[j]) {
					++counter;
					prev = arr[j];
				} else {
					break;
				}
				} else {
					break;
				}
			}
		}
	storage[i] = counter;
	counter = 0;
	prev = -1000000;
	}

	for  (int i = 0; i < n; i++) {
		cout << storage[i] << " ";
	}

	cout << endl;


	// Solve the problem


	// Output the result

	return 0;
}