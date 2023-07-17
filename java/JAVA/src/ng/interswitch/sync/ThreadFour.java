package ng.interswitch.sync;

public class ThreadFour extends Thread{
    SyncTable table;
    ThreadFour(SyncTable table){
        this.table = table;
    }
    public void run(){
        table.printTableSync(4);
    }
}
