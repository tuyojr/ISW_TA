package ng.interswitch.sync;

public class ThreadTwo extends Thread{
    SyncTable table;

    ThreadTwo(SyncTable table){
        this.table = table;
    }
    public void run(){
        table.printTable(10);
    }
}
