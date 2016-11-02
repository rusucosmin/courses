package model;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

/**
 * Created by cosmin on 10/24/16.
 */
public class MyStack <T> implements MyIStack<T> {
    private Stack <T> stack;
    public MyStack(Stack <T> stack) {
        this.stack = stack;
    }

    @Override
    public void push(T el) {
        this.stack.push(el);
    }

    @Override
    public T pop() {
        return this.stack.pop();
    }

    @Override
    public T peek() {
        return this.stack.peek();
    }

    @Override
    public boolean isEmpty() {
        return this.stack.isEmpty();
    }

    @Override
    public String toString() {
        String repr = "";
        MyStack <T> rev = new MyStack<T>(new Stack<T>());
        boolean ok = false;
        while(!this.isEmpty()) {
            if(ok)
                repr = repr + "\n";
            repr += this.peek().toString();
            rev.push(this.pop());
            ok = true;
        }
        while(!rev.isEmpty())
            this.push(rev.pop());
        return repr;
    }
}
