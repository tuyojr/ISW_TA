package ng.interswitch;

//make the class abstract
public abstract class Shape {
    public abstract double area();
    public void printInfo(){
        System.out.println("This is a shape");
    }
}
class Rectangle extends Shape {
    private double length;
    private double width;

    public Rectangle(double length, double width){
        this.length = length;
        this.width = width;
    }

    @Override
    public double area(){
        return length * width;
    }
}

class ShapeTester{
    public static void main(String[] args) {
        Rectangle rectangle = new Rectangle(10, 20);
        System.out.println(rectangle.area());
        rectangle.printInfo();
    }
}
