package ro.dutylabs.web.puzzle;

import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;

/**
 * Created by cosmin on 30/05/2017.
 */
public class PuzzleServlet extends HttpServlet {
    public void writePuzzle(PrintWriter printWriter, String puzzleHtml, int score) {
        printWriter.println("<html>");
        printWriter.println("<head>");
        printWriter.println("<title>Puzzle</title>");
        printWriter.println("<link rel='stylesheet' type='text/css' href='style.css'>");
        printWriter.println("</head>");
        printWriter.println("<body>");
        printWriter.println("<h1>Puzzle!</h1>");
        printWriter.println("<hr>");
        printWriter.println("<div id='puzzle'>");
        printWriter.println(puzzleHtml);
        printWriter.println("</div>");
        printWriter.println("<div id='score'>");
        printWriter.println("<p>Your score is: " + score + "</p>");
        printWriter.println("</div>");
        printWriter.println("<div id='status'>");
        printWriter.println("<p>Keep doing great!</p>");
        printWriter.println("</div>");
        printWriter.println("<hr>");
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
        db.shufflePuzzle();
        writePuzzle(res.getWriter(), db.getPuzzle(), db.getScore());
    }
}
