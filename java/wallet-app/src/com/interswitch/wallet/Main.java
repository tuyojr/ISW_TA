package com.interswitch.wallet;

import com.interswitch.wallet.dto.*;
import com.interswitch.wallet.model.*;
import com.interswitch.wallet.service.WalletService;
import java.util.*;
public class Main {

    static List<Product> productList = new ArrayList<>();
    static List<Cart> cartList = new ArrayList<>();


    public static void main(String[] args) throws Exception {
        WalletService service = new WalletService();
        Product product1 = new Product(1, "Milk", "Peak Milk", 100.00, 100, "2020-01-01", true);
        Product product2 = new Product(2, "Bread", "Agege Bread", 200.00, 100, "2020-01-01", true);
        Product product3 = new Product(3, "Egg", "Fresh Eggs", 50.00, 100, "2020-01-01", true);
        Product product4 = new Product(4, "Biscuit", "Digestive Biscuit", 150.00, 100, "2020-01-01", true);
        Product product5 = new Product(5, "Sausage", "Chicken Sausage", 250.00, 100, "2020-01-01", true);
        Product product6 = new Product(6, "Cheese", "Cheddar Cheese", 350.00, 100, "2020-01-01", true);
        Product product7 = new Product(7, "Butter", "Salted Butter", 450.00, 100, "2020-01-01", true);
        Product product8 = new Product(8, "Yogurt", "Strawberry Yogurt", 550.00, 100, "2020-01-01", true);
        Product product9 = new Product(9, "Ice Cream", "Vanilla Ice Cream", 650.00, 100, "2020-01-01", true);
        Product product10 = new Product(10, "Chocolate", "Dark Chocolate", 750.00, 100, "2020-01-01", true);
        productList.add(product1);
        productList.add(product2);
        productList.add(product3);
        productList.add(product4);
        productList.add(product5);
        productList.add(product6);
        productList.add(product7);
        productList.add(product8);
        productList.add(product9);
        productList.add(product10);

        // use a while loop to keep prompting the user for input until they exit
        while(true){
            System.out.printf("Press %d to add your product to cart.\n", 1);
            System.out.printf("Press %d to checkout.\n", 2);
            System.out.printf("Press %d to get your get your cart contents.\n", 3);
            System.out.printf("Press %d to get the product catalog.\n", 4);
            System.out.printf("Press %d to populate the product catalog.\n", 5);
            System.out.printf("Press %d to restock the product.\n", 6);
            System.out.printf("Press %d to get a product by ID.\n", 7);
            System.out.printf("Press %d to register a customer.\n", 8);
            System.out.printf("Press %d to get a customer by wallet ID.\n", 9);
            System.out.printf("Press %d to fund a customer wallet.\n", 10);
            System.out.printf("Press %d to exit.\n", 0);

            Scanner userValue = new Scanner(System.in);
            System.out.print("Enter your choice: ");
            int choice = userValue.nextInt();

            if (choice == 1){
                Scanner pId = new Scanner(System.in);
                Integer productId = pId.nextInt();
                System.out.print("Enter product ID: ");
                Scanner pQuantity = new Scanner(System.in);
                Integer quantity = pQuantity.nextInt();
                System.out.print("Enter product quantity: ");
                service.addProductToCart(productId, quantity);
                System.out.printf("Product with ID %d and quantity %d added to cart.\n", productId, quantity);
            }
            else if (choice == 2) {
                Scanner wId = new Scanner(System.in);
                String walletId = wId.next();
                System.out.print("Enter wallet ID: ");
                service.checkOutProduct(walletId);
                System.out.printf("User with wallet ID '%s' has checked out.\n", walletId);
            }
            else if (choice == 3) {
                System.out.println("Your cart contains: "); service.getMyProductCart();
            }
            else if (choice == 4) {
                System.out.println("Product catalog: "); service.getProductCatalog();
            }
            else if (choice == 5) {
                service.populateProductCatalog(productList);
                System.out.println("Product catalog populated.");
            }
            else if (choice == 6) {
                Scanner pId = new Scanner(System.in);
                Integer productId = pId.nextInt();
                System.out.print("Enter product ID to be restocked: ");
                Scanner pQuantity = new Scanner(System.in);
                Integer quantity = pQuantity.nextInt();
                System.out.print("Enter product quantity to be restocked: ");
                service.restockProduct(productId, quantity);
                System.out.printf("Product with ID %d and quantity %d added to cart.\n", productId, quantity);
            }
            else if (choice == 7) {
                Scanner pId = new Scanner(System.in);
                Integer productId = pId.nextInt();
                System.out.print("Enter product ID to show availability: ");
                service.getProductById(productId);
            }
            else if (choice == 8) {
                Scanner nm = new Scanner(System.in);
                String name = nm.next();
                System.out.print("Enter customer name to register: ");
                Scanner pN = new Scanner(System.in);
                String phoneNum = pN.next();
                System.out.print("Enter customer phone number: ");
                Scanner addr = new Scanner(System.in);
                String address = addr.next();
                System.out.print("Enter customer address: ");
                service.registerCustomer(name, phoneNum, address);
                System.out.print("Customer registered successfully.\n");
            }
            else if (choice == 9) {
                Scanner wId = new Scanner(System.in);
                String walletId = wId.next();
                System.out.print("Enter wallet ID to get customer: ");
                service.getCustomerByWallet(walletId);
            }
            else if (choice == 10) {
                Scanner wId = new Scanner(System.in);
                String walletId = wId.next();
                System.out.print("Enter wallet ID to fund: ");
                Scanner amt = new Scanner(System.in);
                double amount = amt.nextDouble();
                System.out.print("Enter balance to fund: ");
                service.fundCustomerWallet(walletId, amount);
                System.out.printf("Customer with wallet ID '%s' funded with %n.\n", walletId, amount);
            }
            else if (choice == 0) {
                System.out.println("Thank you four using the Wallet App!!!");
                System.exit(0);
            }
            else {
                System.out.println("Invalid input. Please try again.");
                break;
            }
        }
    }
}
