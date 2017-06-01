package ro.dutylabs.web.puzzle;

import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Stream;

/**
 * Created by cosmin on 30/05/2017.
 */
public class PuzzleServlet extends HttpServlet {
    public void writePuzzle(PrintWriter printWriter, String puzzleHtml, int score) {
        printWriter.println("<html>");
        printWriter.println("<head>");
        printWriter.println("<title>Puzzle</title>");
        printWriter.println("<link rel='stylesheet' type='text/css' href='style.css'>");
        printWriter.println("<script src='scripts/jquery-3.2.1.js'></script>");
        printWriter.println("<script src='scripts/lab9.js'></script> ");
        printWriter.println("</head>");
        printWriter.println("<body>");
        printWriter.println("<h1>Puzzle!</h1>");
        printWriter.println("<hr>");
        printWriter.println("<div id='score'>");
        printWriter.println("<p>Your score is: " + score + "</p>");
        printWriter.println("</div>");
        printWriter.println("<div id='puzzle'>");
        printWriter.println(puzzleHtml);
        printWriter.println("</div>");
        printWriter.println("<div id='status'>");
        printWriter.println("<p id='msg'>Click on an image to make a swap!</p>");
        printWriter.println("<img style='width:100px;height:100px' id='selected'/>");
        printWriter.println("</div>");
        printWriter.println("<hr>");
        printWriter.println("<input action='action' onclick='window.location.href=\"/\"' type='button' value='Back' />");
        printWriter.println("<form action='/puzzle' method='post'> ");
        printWriter.println("<input type='submit' value='Reset puzzle' id='reset'/>");
        printWriter.println("</form>");
        printWriter.println("</body>");
        printWriter.println("</html>");
    }
    public void doGet(HttpServletRequest req, HttpServletResponse res) throws IOException {
        res.setContentType("text/html");
        Database db = new Database();
        db.connect();
        writePuzzle(res.getWriter(), db.getPuzzle(), db.getScore());
   }
    public void doPost(HttpServletRequest req, HttpServletResponse res) throws IOException {
        res.setContentType("text/html");
        Database db = new Database();
        db.connect();
        db.resetGame();
        writePuzzle(res.getWriter(), db.getPuzzle(), db.getScore());
    }
    public void doPut(HttpServletRequest req, HttpServletResponse res) throws IOException {
        System.out.println("Hmmmm poate merge");
        BufferedReader br = new BufferedReader(new InputStreamReader(req.getInputStream()));

        String data = br.readLine();
        System.out.println(data);
        Map<String, String> params = new HashMap<>();
        Stream.of(data.split("&", 2)).forEach((par) -> {
            String[] arr = par.split("=", 2);
            params.put(arr[0], arr[1]);
        });
        int id1 = Integer.valueOf(params.get("id1"));
        int id2 = Integer.valueOf(params.get("id2"));
        System.out.println("changing: " + id1 + " with " + id2);
        Database db = new Database();
        db.connect();
        db.swap(id1, id2);
        db.updateScore(db.getScore() + 1);
        res.getWriter().println(db.getPuzzle());
    }
}
