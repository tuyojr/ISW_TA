package ng.tuyo.jr.uchiha;

import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.time.LocalDate;
import java.util.List;

@Configuration // a configuration class helps to set up the application so that it can input data into the database
public class UchihaConfig {

    @Bean // this annotation is used by Spring boot to know that the method is used to input data into the database
    // the commandLineRunner method is used to input data into the database
    // it is an interface that takes an instance of our repository class as a parameter
    CommandLineRunner commandLineRunner(UchihaRepository repository){
        return args -> {
            Uchiha sasuke = new Uchiha(
                    "Sasuke",
                    "Rinne Sharingan",
                    LocalDate.of(2000, 11, 13)
            );

            Uchiha madara = new Uchiha(
                    "Madara",
                    "10 Tails Jinchuriki",
                    LocalDate.of(1914, 8, 22)
            );

            Uchiha obito = new Uchiha(
                    "Obito",
                    "10 Tails Jinchuriki",
                    LocalDate.of(1989, 2, 16)
            );

            Uchiha itachi = new Uchiha(
                    "Itachi",
                    "Genjutsu",
                    LocalDate.of(1991, 5, 7)
            );

            Uchiha izuna = new Uchiha(
                    "Izuna",
                    "Mangekyo Sharingan",
                    LocalDate.of(1917, 9, 16)
            );

            Uchiha shisui = new Uchiha(
                    "Shisui",
                    "Kotomatsukami",
                    LocalDate.of(1986, 10, 1)
            );

            repository.saveAll(
                    List.of(sasuke, madara, obito, itachi, izuna, shisui)
            );
        };
    }
}
