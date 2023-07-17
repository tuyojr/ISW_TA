package ng.interswitch.input;

public class Implemented implements NewCalculator {
    @Override
    public int addTwoNumbers(int firstNumber, int secondNumber) {
        return firstNumber + secondNumber;
    }

    @Override
    public int subtractTwoNumbers(int firstNumber, int secondNumber) {
        return firstNumber - secondNumber;
    }

    @Override
    public int multiplyTwoNumbers(int firstNumber, int secondNumber) {
        return firstNumber * secondNumber;
    }
}
