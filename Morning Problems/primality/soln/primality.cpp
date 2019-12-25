#include <iostream>
#include <cmath> // for sqrt

using namespace std;

int gcd(unsigned int a,unsigned int b) {
	if (a == 0) {
		return b;
	}
	return gcd(b % a, a);
}

int main() {
    unsigned int n, i;
    bool check = true;
    cin >> n;
    
    for (i=2; i <= sqrt(n);i++) {
    	if(gcd(i,n) == 0)
    	{
    		check = false;
    		break;
    	}
    }

    if (check && n!=1) {
    	cout << "prime" << endl;
    } else {
    	cout << "not prime" << endl;
    }

    

    return 0;
}
