package ro.dutylabs.web.puzzle;

import java.sql.*;
import java.util.Random;

public class Database {
    private String driver;
    private String connString;
    private String user;
    private String pass;
    private Connection con;
    private int n = 3;

    public Database() {
        this.driver = "org.gjt.mm.mysql.Driver";
        this.connString = "jdbc:mysql://localhost:4201/web-lab9";
        this.user = "web-lab9";
        this.pass = "web-lab9";
    }

    public void connect() {
        try {
            Class.forName(driver);
            con = DriverManager.getConnection(connString, user, pass);
        } catch(Exception ex) {
            System.out.println("Error while connecting: "+ex.getMessage());
        }
    }

    public void updateScore(int value) {
        try {
            PreparedStatement pStmt = this.con.prepareStatement("INSERT INTO Puzzle (id, position) VALUES(?, ?) ON DUPLICATE KEY UPDATE position = values(position)");
            pStmt.setInt(1, n * n);
            pStmt.setInt(2, value);
            pStmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void swap(int id1, int id2) {
        try {
            System.out.println("swap ( " + id1 + ", " + id2);
            PreparedStatement pStmtSelect = this.con.prepareStatement("SELECT SUM(position) FROM Puzzle WHERE id IN (?, ?)");
            pStmtSelect.setInt(1, id1);
            pStmtSelect.setInt(2, id2);
            ResultSet rs = pStmtSelect.executeQuery();
            rs.next();
            int sum = Integer.parseInt(rs.getString(1));
            System.out.println("gotSum: " + sum);
            PreparedStatement pStmt = this.con.prepareStatement("UPDATE Puzzle SET position = ? - position WHERE id IN (?, ?)");
            pStmt.setInt(1, sum);
            pStmt.setInt(2, id1);
            pStmt.setInt(3, id2);
            pStmt.executeUpdate();
            System.out.println("updated: " + sum);
        } catch(SQLException e) {
            System.out.println("Error while swapping");
            e.printStackTrace();
        }
    }

    public int getScore() {
        try {
            PreparedStatement pStmt = this.con.prepareStatement("SELECT position FROM Puzzle WHERE id = ?");
            pStmt.setInt(1, n * n);
            ResultSet rs = pStmt.executeQuery();
            if(rs.next())
                return rs.getInt("position");
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return 0;
    }

    public void resetGame() {
        shufflePuzzle();
        updateScore(0);
    }

    static void shuffleArray(int[] ar) {
        Random rnd = new Random();
        for (int i = ar.length - 1; i > 0; i--) {
            int index = rnd.nextInt(i + 1);
            int a = ar[index];
            ar[index] = ar[i];
            ar[i] = a;
        }
    }

    public void shufflePuzzle() {
        Random r = new Random();
        int [] pos = new int[n * n];
        for(int i = 0; i < n * n; ++ i)
            pos[i] = i;
        shuffleArray(pos);
        try {
            for (int i = 0; i < n * n; ++i) {
                PreparedStatement pStmt = this.con.prepareStatement("INSERT INTO Puzzle (id, position) VALUES(?, ?) ON DUPLICATE KEY UPDATE position = values(position)");
                pStmt.setInt(1, i);
                pStmt.setInt(2, pos[i]);
                pStmt.executeUpdate();
            }
        }catch(SQLException e) {
            System.out.println("SqlException: " + e.toString());
            e.printStackTrace();
        }
        System.out.println("shufflePuzzle(): " + pos.toString());
    }

    public String getPuzzle() {
        String res = new String();
        try {
            PreparedStatement stmt = con.prepareStatement("SELECT  * FROM Puzzle where id >= 0 and id < ?");
            stmt.setInt(1, n * n);
            ResultSet rs = stmt.executeQuery();
            int where[] = new int[n * n];
            while(rs.next()) {
                where[rs.getInt("position")] = rs.getInt("id");
            }
            boolean solved = true;
            for(int i = 0; i < n * n; ++ i) {
                if(where[i] != i)
                    solved = false;
                res += "<img id = '" + where[i] + "' class='puzzlepiece' src='img/" + where[i] + ".jpeg'/>";
            }
            if(solved)
                res += "<p>Congratulations, you finished the puzzle in: " + this.getScore() + "!</p>";
        } catch(Exception ex) {
            System.out.println("Error on get Puzzle: " + ex.getMessage());
        }
        return res;
    }
}
