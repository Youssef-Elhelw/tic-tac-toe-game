
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include<numeric>
using namespace std;
int main(){
    int y,w;
    cin>>y;
    cout<<"\n divided by?\n";
    cin>>w;
    if(w==0||y==0){
        cout<<0<<"/"<<1;
    }
    else if(y<w){
        for(int i=w;i>0;i--){
            if(i>=2){
                if(y%i==0&&w%i==0){
                cout<<w/i<<"/"<<y/i;
                break;;      
                }        
            }
            else if(i==1){
                cout<<w<<"/"<<y;
            }
        }
    }else if (y>w){
        for(int i=y;i>0;i--){
            if(i>=2){
                if(y%i==0&&w%i==0){
                cout<<y/i<<"/"<<w/i;
                break;
                }
            }
            else if(i==1){
                cout<<y<<"/"<<w;
            }        
        }
    }else{
        cout<<1<<"/"<<1;
    }
    return 0;
}