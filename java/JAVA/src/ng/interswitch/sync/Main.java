package ng.interswitch.sync;

public class Main {
    public static void main(String[] args) {
        SyncTable table = new SyncTable();
        ThreadOne threadOne = new ThreadOne(table);
        ThreadTwo threadTwo = new ThreadTwo(table);
        threadOne.start();
        threadTwo.start();
    }
}
