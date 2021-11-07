void swap(int *x, int *y) {
	int temp;
	temp = *x;
	*x = *y;
	*y = temp;
	return;
}

#include <iostream>
using namespace std;

int main () {
	int a = 100, b = 200;
	
	cout << "Before swap, values of a, b: " <<a<< ", " <<b<< endl;
	swap(&a, &b);
	cout << "After swap, values of a, b: " <<a<< ", " <<b<< endl;
	
	return 0;
}
