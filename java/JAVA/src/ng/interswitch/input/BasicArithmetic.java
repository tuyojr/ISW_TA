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

    public String squareNumber() {
        double firstSquare = this.firstNumber * this.firstNumber;
        double secondSquare = this.secondNumber * this.secondNumber;
        return ("The square of the first number is = " + firstSquare + "\n" + "The square of the second number is = " + secondSquare);
    }

    // using recursion, set the firstNumber to the power of the secondNumber
    public static int powerRaiser(int number, int powerValue){
        if(powerValue == 0) {
            return 1;
        } else {
            return (number * powerRaiser(number, powerValue-1));
        }
    }
}
