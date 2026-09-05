#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
// 토큰 150 제한을 뚫기위한 풀이 / chatgpt 가 보여줌 / 이런 생각의 전환도 해야함
using namespace std;
int main(){
    int n;
    cin >> n;
    int count[10001]={};
    string names[10001];
    

    for (int t=0; t<n; t++){
        string name;
        int cost;
        cin >> name >> cost;
        count[cost]+=1;
        names[cost]=name;
    }
    string ans = "NONE";
    for (int i=10000; i>=1; i--){
        if (count[i]==1){
            ans=names[i];
            break;
        }
    }
    cout << ans;
    return 0;
}
