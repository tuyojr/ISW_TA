package kotoamatsukami.uchiha.shisui.greet.implementation;

public class Greeting {

    // the constructor class
    public String wetinDeySup(String name){
        return String.format("%s %s", "Wetin dey sup, you don finally start Spring Boot", name);
    }

    // the destroy class
    public void clearRoad(){
        System.out.println(this.getClass().getName() + " don kpeme.");
    }

    // the init class
    public void whoGoes(){
        System.out.println(this.getClass().getName() + " don start.");
    }
}
