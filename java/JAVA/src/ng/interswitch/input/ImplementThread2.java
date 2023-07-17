package ng.interswitch.input;

public class ImplementThread2 implements Runnable{
    @Override
    public void run(){
        for(int x=1; x <=10; x++){
            System.out.printf("%d from runnable dey run ooo..\n", x);
        }
    }
}
