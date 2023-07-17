package ng.interswitch.sync;

public class SyncTable {
    synchronized void printTable(int t){
        for(int i = 1; i < 5; i++){
            System.out.println(t * i);
            try{
                Thread.sleep(400);
            } catch (Exception error){
                System.out.println(error);
            }
        }
    }
}
