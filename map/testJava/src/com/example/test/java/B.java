package com.example.test.java;

/**
 * Created by cosmin on 1/22/17.
 */
public class B {
    public int x;
    public B(int x) {
        this.x = x;
    }
    public static void swap(B b1, B b2) {
        B aux = b1;
        b1 = b2;
        b2 = aux;
    }
    public static void swapCorrect(B b1, B b2) {
        int aux = b1.x;
        b1.x = b2.x;
        b2.x = aux;
    }
}
