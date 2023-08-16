package com.interswitch.tests;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;

import static junit.framework.Assert.*;

@DisplayName(("Write assertions for booleans."))
public class BooleanAssertionTest {

    @Nested
    @DisplayName("When boolean is true.")
    class WhenBooleanIsTrue{
        @Test
        @DisplayName("Should be true.")
        void shouldBeTrue(){
            assertTrue(true);
        }
    }

    @Nested
    @DisplayName("When object is null.")
    class WhenObjectIsNull{
        @Test
        @DisplayName("Should be null.")
        void shouldBeNull(){
            assertNull(null);
        }
    }

    @Nested
    @DisplayName("When objects are integers.")
    class WhenObjectAreIntegers {
        private final Integer ACTUAL = 9;
        private final Integer EXPECTED = 9;

        @Test
        @DisplayName("Should be equal.")
        void shouldBeEqual() {
            assertSame(EXPECTED, ACTUAL);
        }
    }

    @Nested
    @DisplayName("When two objects refer to the same object.")
    class WhenTwoObjectsReferToSameObject {
        private final Object ACTUAL = new Object();
        private final Object EXPECTED = ACTUAL;

        @Test
        @DisplayName("Should refer to the same object.")
        void shouldReferToSameObject() {
            assertSame(EXPECTED, ACTUAL);
        }
    }
}
