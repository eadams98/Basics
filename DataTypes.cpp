#include <iostream>
#include <climits>

using namespace std;

int main()
{

    int yearOfBirth = 1998;
    char gender = 'f';
    bool isOlderThan18 = true;
    float averageGrade = 3.35;
    double balance = 12345678.99;

    cout << "Size of int is " << sizeof(int) << " bytes\n";
    cout << "Int min value is: " << INT_MIN << " int max value is: " << INT_MAX << endl;

    cout << "Size of unsined int is " << sizeof(unsigned int) << " bytes\n";
    cout << "int max value is: " << UINT_MAX << endl;

    cout << "Size of bool is " << sizeof(bool) << " bytes\n";

    cout << "Size of char is " << sizeof(char) << " bytes\n";

    cout << "Size of float is " << sizeof(float) << " bytes\n";

    cout << "Size of double is " << sizeof(double) << " bytes\n";
    

    // DATA TYPE OVERFLOW
    cout << INT_MAX << endl;
    cout << INT_MAX + 1 << endl;

    return 0;
}