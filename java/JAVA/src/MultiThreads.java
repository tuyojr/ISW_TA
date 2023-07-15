public class MultiThreads extends Thread {

    public MultiThreads(String name) {
        super(name);
    }

    public void run() {
        System.out.println("Thread is running... but to where?");
    }

    public static void main(String[] args) {
        MultiThreads t1 = new MultiThreads("Na me dey run this thing!");
        t1.start();
        String name = t1.getName();
        System.out.println("Thread name is: " + name);
    }
}
