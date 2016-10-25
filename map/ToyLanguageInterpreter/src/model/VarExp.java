package model;

import exception.UnknownVariableException;

/**
 * Created by cosmin on 10/25/16.
 */
public class VarExp extends Exp {
    private String id;

    public VarExp(String id) {
        this.id = id;
    }

    @Override
    public int eval(MyIDictionary<String, Integer> symTable) {
        try {
            return symTable.get(id);
        } catch (UnknownVariableException e) {
            e.printStackTrace();
        }
        return -1;
    }

    @Override
    public String toStr() {
        return id;
    }
}
