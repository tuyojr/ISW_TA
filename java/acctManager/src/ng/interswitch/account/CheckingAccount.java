package ng.interswitch.account;
import java.io.*;
public class CheckingAccount {
    public double getBalance() {
        return balance;
    }

    public int getAcctNumber() {
        return acctNumber;
    }

    private double balance;
    private int acctNumber;

    public CheckingAccount(int acctNumber) {
        this.acctNumber = acctNumber;
    }

    public void deposit(double amount) {
        balance += amount;
    }

    public void withdraw(double amount) throws InsufficientFundsException {
        if (amount <= balance) {
            balance -= amount;
        } else {
            double needs = amount - balance;
            throw new InsufficientFundsException(needs);
        }
    }
}
