package com.interswitch.tests;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertThrows;


@DisplayName("Writing assertions for exceptions.")
public class ExceptionAssertionTest {

    @Test
    @DisplayName("Should throw the correct exception.")
    void shouldThrowCorrectException() {
        assertThrows(
                NullPointerException.class,() -> {throw new NullPointerException();}
        );
    }
}
