package view;

import model.Command;
import model.MyIDictionary;

import java.util.Scanner;

/**
 * Created by cosmin on 02/11/16.
 */
public class TextMenu {
    private MyIDictionary<String, Command> cmds;
    public TextMenu(MyIDictionary<String, Command> cmds) {
        this.cmds = cmds;
    }
    public void addCommand(Command cmd) {
        this.cmds.put(cmd.getKey(), cmd);
    }
    public void printMenu() {
        System.out.println("Available commands: ");
        for(Command cmd : this.cmds.values()) {
            String line = String.format("Command %4s: %s", cmd.getKey(), cmd.getDescription());
            System.out.println(line);
        }
    }

    public void show() {
        Scanner scanner = new Scanner(System.in);
        while(true) {
            printMenu();
            System.out.println("Input the command: ");
            Command cmd = cmds.get(scanner.nextLine());
            if(cmd == null) {
                System.out.println("Invalid command");
                continue;
            }
            cmd.execute();
        }
    }
}
