package ng.tuyo.jr;

import ng.tuyo.jr.uchiha.Uchiha;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.time.LocalDate;
import java.util.List;

@SpringBootApplication // makes the class serve as a spring boot application
public class JrApplication {

	// the main method is the entry point of the application
	// SpringApplication.run(JrApplication.class, args) starts the application
	public static void main(String[] args) {
		SpringApplication.run(JrApplication.class, args);
	}
}
