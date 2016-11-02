package model;

/**
 * Created by cosmin on 02/11/16.
 */
public class ExitCommand extends Command {
    public ExitCommand(String key, String descr) {
        super(key, descr);
    }

    @Override
    public void execute() {
        System.out.println("Bye bye!");
        System.exit(0);
    }
}
