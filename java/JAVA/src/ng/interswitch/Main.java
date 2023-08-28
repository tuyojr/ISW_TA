package ng.interswitch;

public class Main {
    public static void main(String[] args) {
        Circle circle = new Circle();
        circle.draw();

        Rectangle rectangle = new Rectangle(10, 20);
        System.out.println(rectangle.area());
    }
}
