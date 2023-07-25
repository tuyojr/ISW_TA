package kotoamatsukami.uchiha.shisui;

import kotoamatsukami.uchiha.shisui.greet.Greeting;
import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class ShisuiApplication implements ApplicationRunner {

	private final Greeting greeting;

	public ShisuiApplication(Greeting greeting) {
		this.greeting = greeting;
	}

	public static void main(String[] args) {
		SpringApplication.run(ShisuiApplication.class, args);
	}

	@Override
	public void run(ApplicationArguments args) throws Exception {
		System.out.println(greeting.wetinDeySup("Itachi"));
	}

	public Greeting getGreeting() {
		return greeting;
	}
}
