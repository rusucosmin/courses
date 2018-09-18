package com.example.test.java;

public class Main {

    public static void main(String[] args) {
	// write your code here
        B b1 = new B(1);
        B b2 = new B(2);
        B.swap(b1, b2);
        B.swapCorrect(b1, b2);
        System.out.println(b1.x + " " + b2.x);
    }
}
