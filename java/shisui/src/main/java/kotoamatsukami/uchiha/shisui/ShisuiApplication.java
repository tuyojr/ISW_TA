package kotoamatsukami.uchiha.shisui;

import kotoamatsukami.uchiha.shisui.greet.Greet;
import kotoamatsukami.uchiha.shisui.greet.implementation.Greeting;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class ShisuiApplication implements ApplicationRunner {

	private final Greeting greeting;

	private final Greet greet;

	@Value(value="${application_name:genjutsu-app}")
	private String applicationName;

	public ShisuiApplication(@Autowired Greeting greeting, Greet greet) {
		this.greeting = greeting;
		this.greet = greet;
	}

	@Override
	public void run(ApplicationArguments args) throws Exception {
		System.out.println(greeting.wetinDeySup("Itachi"));
		greet.wagwan();
		System.out.println(applicationName);
	}

	public static void main(String[] args) {
		SpringApplication.run(ShisuiApplication.class, args);
	}
}
