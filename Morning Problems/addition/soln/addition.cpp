#include <iostream>
#include <algorithm>

using namespace std;

int main() {
  int n;
  cin >> n;

  long a[100000];
  long b[100000];
  long sum[100001];


  for (int i = n-1; i >= 0; --i) {
  	cin >> a[i];
  }
  
  for (int i = n-1; i >= 0; --i) {
  	cin >> b[i];
  }
 

  for (int i = 0; i < n; ++i) {
  	if (i == n - 1) {
  		sum[i] = a[i] + b[i];
  	} else if (a[i] + b[i] >= 10) {
  		sum[i] = ((a[i] + b[i]) - 10);
  		++a[i+1];
  	} else {
  		sum[i] = a[i] + b[i];
  	}
  }

  for (int i = n-1; i >= 0; --i) {
   	cout << sum[i];
  }

  cout << endl;
  return 0;
}