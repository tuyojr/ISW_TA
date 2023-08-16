package com.interswitch.tests;

import org.junit.jupiter.api.*;

public class PerMethodLifecycleTest {
    public PerMethodLifecycleTest() {
        System.out.println("Constructor.");
    }

    @BeforeAll
    static void beforeTheEntireTestFixture() {
        System.out.println("Before the entire test fixture.");
    }

    @AfterAll
    static void afterTheEntireTestFixture() {
        System.out.println("After the entire test fixture.");
    }

    @BeforeEach
    void beforeEachTest() {
        System.out.println("Before each test.");
    }

    @AfterEach
    void afterEachTest() {
        System.out.println("After each test.");
    }

    @Test
    void firstTest() {
        System.out.println("First test.");
    }

    @Test
    void secondTest() {
        System.out.println("Second test.");
    }
}
