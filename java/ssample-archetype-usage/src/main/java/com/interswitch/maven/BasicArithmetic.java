package com.interswitch.maven;

public class BasicArithmetic {

    private double firstNumber;

    private double secondNumber;

    public double getFirstNumber() {
        return firstNumber;
    }

    public double getSecondNumber() {
        return secondNumber;
    }

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

    public double multiplyFirstAndSecondNumber() {
        return this.firstNumber * this.secondNumber;
    }

    public double divideFirstAndSecondNumber() {
        return this.firstNumber / this.secondNumber;
    }
}
