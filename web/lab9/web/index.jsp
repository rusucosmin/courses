<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Puzzle</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    <h1>Puzzle Game</h1>
    <nav>
        <form action="/puzzle" method="get">
            <input type="submit" value="Continue the puzzle" id="continue"/>
        </form>
        <form action="/puzzle" method="post">
            <input type="submit" value="Reset puzzle" id="reset"/>
        </form>
    </nav>
</body>
</html>
