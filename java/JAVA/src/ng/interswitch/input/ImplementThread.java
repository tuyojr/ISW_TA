package ng.interswitch.input;

public class ImplementThread extends Thread{
    @Override
    public void run(){
        super.run();
        for (int i = 1; i <= 10; i++){
            System.out.printf("%d is printing from the ImplementThread class..\n", i);
        }
    }
}
