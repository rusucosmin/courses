#Exam

##Minimum cost walk by dynamic programming
- Let `dp[k][x]` = the minimum cost walk of at most k edges from s to x
- So `dp[0][s] = 0` and `dp[0][x] = oo for every x != s`
- dp[k][x] = min({dp[k - 1][y] | (y, x) is an edges in the Graph)
- Small piece of code:

```c++
    memset(dp, oo, sizeof(dp));
    dp[0][s] = 0;
    for(int k = 1; k < n; ++ k)
        for(int i = 1; i <= n; ++ i)
            for(auto it : gt[node]) /// on the transpose graph. the list gt[node] contains pairs (nextNode, edgeCost)
                dp[k][it.first] = min(dp[k][it.first], dp[k - 1][it.first] + it.second)
    /// the solutions lies on dp[n - 1][t]
```
