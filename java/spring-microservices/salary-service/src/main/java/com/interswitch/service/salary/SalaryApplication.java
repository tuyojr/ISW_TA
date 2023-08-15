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
		repository.add(new Salary(1L, 2718392L, "1989-11-19"));
		repository.add(new Salary(1L, 3782943L, "1990-04-18"));
		repository.add(new Salary(2L, 7498300L, "1978-01-03"));
		repository.add(new Salary(2L, 9230432L, "1988-11-15"));
		repository.add(new Salary(3L, 2032303L, "1996-10-22"));
		repository.add(new Salary(3L, 2383431L, "2000-06-11"));
		return repository;
	}
}
