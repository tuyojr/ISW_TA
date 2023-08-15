package com.interswitch.service.salary;

import com.interswitch.service.salary.repository.SalaryRepository;
import io.swagger.v3.oas.annotations.OpenAPIDefinition;
import io.swagger.v3.oas.annotations.info.Info;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.openfeign.EnableFeignClients;
import org.springframework.context.annotation.Bean;
import com.interswitch.service.salary.model.Salary;

@SpringBootApplication
@EnableFeignClients
@OpenAPIDefinition(info =
	@Info(title = "Salary API", version = "1.0", description = "Documentation Salary API v1.0")
)
public class SalaryApplication {

	public static void main(String[] args) {
		SpringApplication.run(SalaryApplication.class, args);
	}
	
	@Bean
	SalaryRepository repository() {
		SalaryRepository repository = new SalaryRepository();
		repository.add(new Salary(1L, "Development"));
		repository.add(new Salary(1L, "Operations"));
		repository.add(new Salary(2L, "Development"));
		repository.add(new Salary(2L, "Operations"));
		return repository;
	}
	
}
