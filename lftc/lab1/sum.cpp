int main()
{
  int n; int sum; int ind; int x;
  cin >> n;
  sum = 0;
  ind = 0;
  while (ind < n) {
    cin >> x;
    sum = sum + x;
    ind = ind + 1;
  }
  cout << sum;
  return 0;
}
