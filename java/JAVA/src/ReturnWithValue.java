class ReturnWithValue {
    int sum(int a, int b) {
        return a + b;
    }

    int difference(int a, int b) {
        return a - b;
    }

    // public so that it can be accessed from outside the class
    // static so that it can be accessed without creating an object of the class
    // void because does not return a value
    // main is the name of the method
    // String[] args is the parameter passed to the main method by the JVM
    public static void main(String[] args) {
        ReturnWithValue obj = new ReturnWithValue();
        int sum = obj.sum(10, 20);
        int difference = obj.difference(10, 20);
        System.out.println("Sum: " + sum);
        System.out.println("Difference: " + difference);
    }

    // static block will always be executed before main method
    static {
        System.out.println("This is a static block");
    }
}
