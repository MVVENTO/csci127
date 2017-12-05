#include <iostream>
using namespace std;

int main() 
{
  int num;
  cout << "Hello!";
  cout << "Enter a number: ";
  cin >> num;
  cout<<num<<endl;
  cout<<(num%2)<<endl;
  if (num % 2 == 0)
  {
    cout << "Even number!\n";
  }
  else
  {
    cout << "Odd number\n";
  }
  return 0;
}
