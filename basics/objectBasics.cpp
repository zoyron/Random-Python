#include <bits/stdc++.h>
using namespace std;

class test{
  int age = 100;
  int car = 8000;

  public:
  
  void show_age(){
    cout << "the age is " << age << endl;
  }

  void show_car(){
    cout << "the car plate number is " << car << endl;
  }
};

int main(){
  test ob1 = test();
  ob1.show_age();
  ob1.show_car();
  return 0;
}

