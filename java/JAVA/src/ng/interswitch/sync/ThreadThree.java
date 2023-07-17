package ng.interswitch.sync;

public class ThreadThree extends Thread {
    SyncTable table;
    ThreadThree(SyncTable table){
        this.table = table;
    }

    public void run(){
        table.printTableSync(3);
    }
}
