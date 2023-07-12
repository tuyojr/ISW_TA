class ReturnWithoutValue {
    // void is used to declare method that does not return a value
    void increment(int number) {
        if (number < 10) return;
        number ++;
        System.out.println(number);
    }

    public static void main(String[] args) {
        ReturnWithoutValue obj = new ReturnWithoutValue();
        obj.increment(4);
        obj.increment(11);
    }
}
