package ng.interswitch.input;

public class Main {
    public static void main(String[] args) {
        ImplementThread implementThread = new ImplementThread();
        implementThread.start();
        ImplementThread2 implement2 = new ImplementThread2();
//        implement2.run();
        Thread runnableThread = new Thread(implement2);
        runnableThread.start();
        for(int x=1; x <=10; x++){
            System.out.printf("%d is printing from the main class..\n", x);
        }
    }
}
