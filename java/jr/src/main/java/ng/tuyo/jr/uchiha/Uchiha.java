package ng.tuyo.jr.uchiha;

import java.time.LocalDate;

public class Uchiha {
    private Long id;
    private String name;
    private String powerUp;
    private LocalDate date_of_birth;
    private Integer age;

    public Uchiha() {}

    public Uchiha(Long id,
                  String name,
                  String powerUp,
                  LocalDate date_of_birth,
                  Integer age) {
        this.id = id;
        this.name = name;
        this.powerUp = powerUp;
        this.date_of_birth = date_of_birth;
        this.age = age;
    }

    public Uchiha(String name,
                  String powerUp,
                  LocalDate date_of_birth,
                  Integer age) {
        this.name = name;
        this.powerUp = powerUp;
        this.date_of_birth = date_of_birth;
        this.age = age;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getPowerUp() {
        return powerUp;
    }

    public void setPowerUp(String powerUp) {
        this.powerUp = powerUp;
    }

    public LocalDate getDate_of_birth() {
        return date_of_birth;
    }

    public void setDate_of_birth(LocalDate date_of_birth) {
        this.date_of_birth = date_of_birth;
    }

    public Integer getAge() {
        return age;
    }

    public void setAge(Integer age) {
        this.age = age;
    }

    @Override
    public String toString() {
        return "Uchiha{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", powerUp='" + powerUp + '\'' +
                ", date_of_birth=" + date_of_birth +
                ", age=" + age +
                '}';
    }
}
