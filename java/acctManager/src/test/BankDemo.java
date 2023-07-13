package test;
import ng.interswitch.account.CheckingAccount;
import ng.interswitch.account.InsufficientFundsException;

import java.io.*;
public class BankDemo {
    public static void main(String[] args) {
        CheckingAccount muffin = new CheckingAccount(342521622);
        System.out.println("Depositing $511750...");
        muffin.deposit(511750.00);

        try{
            System.out.println("\nWithdrawing $100000...");
            muffin.withdraw(100000.00);
            System.out.println("\nWithdrawing $800000...");
            muffin.withdraw(800000.00);
        } catch(InsufficientFundsException e) {
            System.out.println("Sorry, but you are short $" + e.getAmount());
            e.printStackTrace();
        }
    }
}
