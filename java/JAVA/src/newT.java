class newT extends Thread{
    Thread t1;
    Thread t2;
    newT(){
        t1 = new Thread(this, "T_1");
        t2 = new Thread(this, "T_2");
        t1.start();
        t2.start();
    }
    public void run(){
        t2.setPriority(Thread.MAX_PRIORITY);
        System.out.print(t1.equals(t2));
    }
}
class mTP{
    public static void main(String[] args){
        new newT();
    }
}
