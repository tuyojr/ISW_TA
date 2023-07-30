package ng.tuyo.jr.uchiha;

import jakarta.persistence.*;

import java.time.LocalDate;
import java.time.Period;

@Entity // makes the class serve as an entity and maps it to a table in the database. It is for hibernate.
@Table // maps the class to a table in the database.
public class Uchiha {

    @Id // makes the id field the primary key of the table
    @SequenceGenerator(
            name = "uchiha_sequence",
            sequenceName = "uchiha_sequence",
            allocationSize = 1
    ) // a sequence generator is used to generate the id of the table
    @GeneratedValue(
            strategy = GenerationType.SEQUENCE,
            generator = "uchiha_sequence"
    ) // the id is generated automatically
    private Long id;
    private String name;
    private String powerUp;
    private LocalDate date_of_birth;

    @Transient // makes sure this field doesn't need to be a column in our database. It is calculated for us.
    private Integer age;

    public Uchiha() {}

    public Uchiha(Long id,
                  String name,
                  String powerUp,
                  LocalDate date_of_birth) {
        this.id = id;
        this.name = name;
        this.powerUp = powerUp;
        this.date_of_birth = date_of_birth;
    }

    public Uchiha(String name,
                  String powerUp,
                  LocalDate date_of_birth) {
        this.name = name;
        this.powerUp = powerUp;
        this.date_of_birth = date_of_birth;
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
        return Period.between(this.date_of_birth, LocalDate.now()).getYears();
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
