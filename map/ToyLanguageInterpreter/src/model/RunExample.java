package model;

import controller.Controller;
import exception.*;

import java.io.IOException;

/**
 * Created by cosmin on 02/11/16.
 */
public class RunExample extends Command {
    Controller ctrl;
    public RunExample(String key, String desc, Controller ctrl) {
        super(key, desc);
        this.ctrl = ctrl;
    }
    @Override
    public void execute() {
        try {
            this.ctrl.allSteps();
        } catch (UnknownVariableException e) {
            System.out.println(e.getMessage());
            return ;
        } catch (DivideByZeroException e) {
            System.out.println(e.getMessage());
            return ;
        } catch (FileAlreadyOpenedException e) {
            System.out.println(e.getMessage());
            return ;
        } catch (FileNotOpenedException e) {
            System.out.println(e.getMessage());
            return ;
        } catch (IOException e) {
            System.out.println(e.getMessage());
            return ;
        } catch (NullPointerException n) {
            System.out.println(n.getMessage());
            return ;
        } catch (UnknownComparisonExpression e) {
            System.out.println(e.getMessage());
            return ;
        }
    }
}
