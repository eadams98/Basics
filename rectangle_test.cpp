#include <iostream>
#include "rectangle.h"

using namespace std;

int main() {
	Rectangle rect1(5,5);
	cout<< "Area of rect1: " << rect1.area() << endl;
	
	Rectangle * rect2;
	rect2 = new Rectangle(3,4);
	cout << "Area of rect2: " << (*rect2).area() << endl;
	cout << "Area of rect2: " << rect2->area() << endl;
	delete rect2;
	
	return 0;
}
