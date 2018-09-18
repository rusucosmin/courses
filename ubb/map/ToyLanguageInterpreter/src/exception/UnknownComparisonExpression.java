package exception;

import com.sun.org.apache.xalan.internal.extensions.ExpressionContext;

/**
 * Created by cosmin on 11/15/16.
 */
public class UnknownComparisonExpression extends Exception {
    public UnknownComparisonExpression(String s) {
        super(s);
    }
}
