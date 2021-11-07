#include <iostream>

using namespace std;

int main()
{

    int number;
    
    cout << "Please enter a whole number: ";
    cin >> number;
    cout << number << endl;

    /*if (number % 2 == 0) {
        cout << "Your number is even" << endl;
    } else {
        cout << "Your number is odd" << endl;
    }*/

    (number % 2 == 0)? 
    cout << "your number is even" << endl :
    cout << "your number is odd" << endl;
    
    //system("clear");

    return 0;
}