package test;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
public class CalculatorTester {
    @Test
    public void testAdd() {
        Calculator calculator = new Calculator();
        Integer result = calculator.add(5, 3);
        Assertions.assertEquals(8, result);
    }
    @Test
    public void testSubtract() {
        Calculator calculator = new Calculator();
        Integer result = calculator.subtract(10, 4);
        Assertions.assertEquals(6, result);
    }
}
