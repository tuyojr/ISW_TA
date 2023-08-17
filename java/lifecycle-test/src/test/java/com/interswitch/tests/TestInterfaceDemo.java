package com.interswitch.tests;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
public class TestInterfaceDemo implements TestLifecycleLogger,
    TestInterfaceDynamicTestDemo {
    @org.junit.jupiter.api.Test
    void isEqualValue() {
        assertEquals(1, "a".length(), "is always equal.");
    }
}
