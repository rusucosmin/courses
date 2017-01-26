package com.example.test.java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collector;
import java.util.stream.Collectors;

class Person {

}

class Employee extends Person {

}

interface I {
}

class A implements I {
}

class B extends A {
}

class C extends A {
}

public class Main {

    public static void ex1() {
        List<String> words = Arrays.asList("hi", "hello", "java8", "lambda");
        words.stream()
                .forEach((e) -> {
                    System.out.println("  " + e);
                });
    }

    public static void ex2() {
        List<String> words = Arrays.asList("hi", "hello", "java8", "lambda");
        words.stream()
                .forEach(System.out::println);
    }

    public static void ex3() {
        List<String> words = Arrays.asList("hi", "hello", "java8", "lambda");
        List<String> excitingWords = words.stream()
                //.map(s -> s + "!")
                //.map(s -> s.replace("i", "eye"))
                .map(s -> s.toUpperCase())
                .collect(Collectors.toList());
        excitingWords.stream()
                .forEach(System.out::println);
    }

    public static void ex4() {
        List<String> words = Arrays.asList("hi", "hello", "java8", "lambda");
        words.stream()
                //.filter(e -> e.length() < 4)
                .collect(Collectors.toList())
                .stream()
                .forEach(System.out::println);
    }

    public static void ex5() {
        List<String> words = Arrays.asList("hi", "he", "elo", "hello", "java8", "lambda");
        words.stream()
                .map(e -> e.toUpperCase())
                .filter(e -> e.length() < 4)
                .filter(e -> e.contains("E"))
                .collect(Collectors.toList())
                .stream()
                .forEach(System.out::println);
    }

    public static void ex6() {
        List<String> words = Arrays.asList("hi", "he", "elo", "hello", "java8", "lambda");
        System.out.println(words.stream()
                .reduce("",
                        (acc, e) -> acc + e.toUpperCase()
                )
        );
    }

    public static void ex7() {
        List<String> words = Arrays.asList("hi", "he", "elo", "hello", "java8", "lambda");
        System.out.println(words.stream()
                .map(e -> e.toUpperCase())
                .reduce((acc, e) -> acc + e)
                .get());
    }
    public static void ex8() {
        List<String> words = Arrays.asList("hi", "he", "elo", "hello", "java8", "lambda");
        System.out.println(words.stream()
                .collect(Collectors.joining(", ")));
    }
    public static void ex9() {
        List<String> words = Arrays.asList("hi", "he", "elo", "hello", "java8", "lambda");
        System.out.println(
                words.stream()
                .map(e->e.length())
                .reduce(0, (a, b) -> a + b)
        );
    }
    public static void ex10() {
        List<String> words = Arrays.asList("hi", "he", "elo", "hello", "java8", "lambdah");
        System.out.println(
            words.stream()
                .filter(e -> e.contains("h"))
                .count()
        );
    }
    public static int test() {
        try {
            throw new Exception("mata");
        } catch(Exception e) {
            return 2;
        } finally {
            return 3;
        }
    }
    public static void main(String[] args) {
        System.out.println(test());
	    // write your code here
//        I test = new C();
//        I test1 = new B();
//        I test2 = new A();
        //ex1()
        //ex2()
        //ex3()
        //ex4()
        //ex5()
        //ex6()
        //ex7()
        //ex8()
        //ex9()
        //ex10();
        /*
        List<String> ls = new ArrayList<String>();
        ls.add("mere");
        ls.add("pere");
        List<?> li = ls;
    //    li.add("portocale");
     //   li.update(1, "struguri");
        Object el = li.get(0);
        li.append(null);
        */
//        List<Employee> la = new ArrayList<Employee>();
//        la.add(new Employee());
//        List<? extends Person> lp = la;
//        Object x = lp.get(0);
//        Person y = lp.get(0);
//        List<? super Person> ls = la;
//        Object x = lp.get(0);
//        Person y = lp.get(0);
//        Employee z = lp.get(0);
//        ls.add(new Person());
//        ls.add(new Employee());
//        ls.add(new Object());
//        lp.add(new Angajat());
//        lp.add(new Object());
//        lp.add(new Person());
//        List<A> list1 = new ArrayList<A>();
//        List<B> list2 = new ArrayList<B>();
//        List<C> list3 = new ArrayList<C>();
//        process(list1);
//        process(list2);
//        process(list3);
//        List<?> wildlist;
//        List<Integer> intlist = new ArrayList<Integer>();
//        wildlist = intlist;
//        intlist.add(new Integer(10));
//        wildlist.add(null);
//        Integer a = intlist.get(0);
//        Object b = wildlist.get(0);

        ArrayList<?> wildlist;
        ArrayList<Integer> intlist = new ArrayList<Integer>();
        wildlist = intlist;
        intlist.add(0, new Integer(2));
        wildlist.add(1, null);
        Integer a = intlist.get(1);
        Object b = wildlist.get(1);
    }
    static void process(List<A> list) {
    }
}

class Complex{
    private double real, imag;
    // constructors ...
    public void aduna (double real){
        this.real+=real;
    }
    public void aduna(Complex c){
        this.real+=c.real;
        this.imag+=c.imag;
    }
    /*
    public Complex aduna(Complex cc){
        this.real+=cc.real;
        this.imag+=cc.imag;
        return this;
    }
    */
}
