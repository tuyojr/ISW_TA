package ng.tuyo.jr;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication // makes the class serve as a spring boot application
public class JrApplication {

	// the main method is the entry point of the application
	// SpringApplication.run(JrApplication.class, args) starts the application
	public static void main(String[] args) {
		SpringApplication.run(JrApplication.class, args);
	}
}
