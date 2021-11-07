#include <iostream>

using namespace std;

int main()
{

    float num1, num2;
    char operation;

    /*
    cout << "Enter your first number: ";
    cin >> num1;
    cout << "Enter your operator: ";
    cin >> operation;
    cout << "Enter your Second number: ";
    cin >> num2;
    */

   cin >> num1 >> operation >> num2;
   
   switch (operation)
   {
   case '*':
       cout << num1 * num2 << endl;
       break;
   case '/':
       cout << num1 / num2 << endl;
       break;
    case '+':
       cout << num1 + num2 << endl;
       break;
    case '-':
       cout << num1 - num2 << endl;
       break;
    case '%':
        bool num1IsInt, num2IsInt;
        num1IsInt = (int) num1 == num1;
        num2IsInt = int(num2) == num2;
        if (num1IsInt && num2IsInt) {
            cout << (int) num1 % int(num2) << endl;
        } else {
            cout << "NOT VALID OPERATION. NUM OF TYPE FLOAT" << endl;
        }
        break;
   default:
        cout << "ERROR";
        break;
   }

   system("clear");

   int year, month;
   cin >> year >> month;

   switch (month)
   {
   case 2: (year % 4 == 0 && year % 100 != 0 or year % 400 == 0)?
       cout << "29 days in the month":
       cout << "28 days in the month";
       break;
    case 4: case 6: case 9: case 11:
       cout << "30 days in the month";
       break;
    case 1: case 3: case 5: case 7: case 8: case 10: case 12:
        cout << "31 days a month";
   default:
        cout << "NOT A VALID MONTH";
        break;
       
   }

    return 0;
}