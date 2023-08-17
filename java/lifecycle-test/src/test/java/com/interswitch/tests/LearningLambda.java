package com.interswitch.tests;


import org.junit.jupiter.api.DynamicTest;
import org.junit.jupiter.api.TestFactory;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

import java.util.List;
import java.util.stream.Stream;

import static com.interswitch.tests.TestInterfaceDynamicTestDemo.Test.isPalindrome;
import static org.junit.jupiter.api.Assertions.assertTrue;
public class LearningLambda {

    public static void main(String[] args) {
        Stream.of("racecar", "mum", "game")
                .map(t -> {
                    t.concat("-good");
                    return t;
                }).forEach(c -> printValue(c));
        System.out.println("=======");
        List.of("Sugar", "Bread", "Tea")
                .stream().map(b -> "ingredient".concat(b))
                .forEach(i -> printValue(i));
    }

    private static void printValue(String s) {
        System.out.println(s);
    }

    @ParameterizedTest
    @ValueSource(ints= {1, 3, 5, -3, 15, Integer.MAX_VALUE})
    void parameterizedTest(int number) {
        assertTrue(Numbers.isOdd(number));
    }

    @ParameterizedTest
    @ValueSource(strings = {"", " "})
    void isBlank_ShouldReturnTrueForNullOrBlankStrings(String input) {
        assertTrue(Strings.isBlank(input));
    }
}

interface TestInterfaceDynamicTestDemo {
    @TestFactory
    default Stream<DynamicTest> dynamicTestsForPalindromes() {
        return Stream.of("racecar", "radar", "mom", "dad")
                .map(text -> DynamicTest.dynamicTest(text, () -> assertTrue(isPalindrome(text))));
    }
    class Test {
        public static boolean isPalindrome(String text) {
            return text.contains("da") ? true : false;
        }
    }
}