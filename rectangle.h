#ifndef RECTANGLE_H
#define RECTANGLE_H

using namespace std;

class Rectangle {
	public:
		Rectangle (int a=0, int b=0);
		~Rectangle();
		int area();
		
	private:
		int width, height;
	};
	
#endif
