#include<bits/stdc++.h>

#define FOR(i, a, b) for(int i=a; i<b; ++i)
using namespace std;
typedef long long LL;
const  int maxn = 1e2 + 5;
int n,dp[maxn][maxn][2], a[maxn];

int main(){
    ios::sync_with_stdio(false);
    // take input for length
    cin >> n;
    // take input for data list  
    FOR(i, 1, n+1){
        cin >> a[i];
        if(a[i] == 0) a[i] = -1;
        else a[i] %= 2;
    }
    //initialization
    FOR(i, 0, maxn)
        FOR(j, 0, maxn)
            dp[i][j][0] = dp[i][j][1] = 1e9;
    dp[0][0][0] = dp[0][0][1] = 0;
    //dp
    FOR(i, 1, n+1)
        FOR(j, 0, i+1){
            if(a[i] != 1) dp[i][j][0] = min(dp[i-1][j-1][0], dp[i-1][j-1][1] + 1); //fit even
            if(a[i] != 0) dp[i][j][1] = min(dp[i-1][j][0] + 1, dp[i-1][j][1]); //fit odd
        }
    cout << min(dp[n][n/2][0], dp[n][n/2][1]) << endl;
    return 0;
}