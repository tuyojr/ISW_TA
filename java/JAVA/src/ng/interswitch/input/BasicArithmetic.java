package ng.interswitch.input;

public class BasicArithmetic {

    private double firstNumber;

    private double secondNumber;

    public void setFirstNumber(double firstNumber) {
        this.firstNumber = firstNumber;
    }

    public void setSecondNumber(double secondNumber) {
        this.secondNumber = secondNumber;
    }
    public BasicArithmetic(double firstNum, double secondNum) {
        this.firstNumber = firstNum;
        this.secondNumber = secondNum;
    }

    public double addFirstAndSecondNumber() {
        return this.firstNumber + this.secondNumber;
    }

    public double subtractFirstAndSecondNumber() {
        return this.firstNumber - this.secondNumber;
    }
}
