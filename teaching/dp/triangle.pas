Program pascal;
uses math;
type
    matrix = array[1..100, 1..100] of integer;
var f: file of integer;
    i, j, n, m: integer;
    a, dp: matrix;
begin
    Assign(f, 'triangle.in');
    read(f, n);
    read(f, m);

    for i := 1 to n do
        for j := 1 to m do
            read(f, a[i][j]);

    for i := 1 to n do
        dp[n][i] := a[n][i];

    for i := n - 1 downto 1 do
        for j := 1 to i do
            dp[i][j] := a[i][j] + Max(dp[i + 1][j], dp[i + 1][j + 1]);

    write(dp[1][1], '\n1 1\n');
    j := 1;
    for i := 2 to n do begin
        if dp[i][j] < dp[i][j + 1] then
            j := j + 1;
        write(i, ' ', j);
    end;

    Close(f);
end.
