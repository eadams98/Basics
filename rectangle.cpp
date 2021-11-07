#include <iostream>
#include "rectangle.h"

using namespace std;

Rectangle::Rectangle (int a, int b): width(a), height(b) {
	cout<< "Object is being crated" << endl;
}

Rectangle::~Rectangle() {
	cout << "Object is being delted" << endl;
}

int Rectangle::area () {
	return (width*height);
}
