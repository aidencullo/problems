#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
  bool isMatch(string s, string p) {
    return func(s, p, s.size()-1, p.size()-1);
  }
  bool func(string& s, string& p, int m, int k){
      if(m < 0 && k < 0) return true;
      if(m >= 0 && k < 0) return false;
      if(m < 0 && k >= 0){
	while(k >= 0 && p[k] == '*') k--;
	return k < 0;
      }

      if(p[k] == '*'){
	while(k >= 0 && p[k] == '*') k--;
	k++;
	return func(s, p, m-1, k-1) || func(s, p, m-1, k) || func(s, p, m, k-1);
      }
      if(p[k] == '?'){
	return func(s, p, m-1, k-1);
      }
      if(p[k] == s[m]){
	return func(s, p, m-1, k-1);
      }
      return false;
    }
};


int main(){
  Solution s;
  cout << s.isMatch("aa","*") << endl;
  cout << s.isMatch("","******") << endl;
  cout << s.isMatch("aab","c*a*b") << endl;
  return 0;
}
