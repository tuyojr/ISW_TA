package ng.interswitch.sync;

public class ThreadOne extends Thread{
    SyncTable table;
    ThreadOne(SyncTable table){
        this.table = table;
    }
    public void run(){
        table.printTable(5);
    }
}
