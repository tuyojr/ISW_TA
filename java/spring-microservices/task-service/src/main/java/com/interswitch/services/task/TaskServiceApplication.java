package com.interswitch.services.task;

import com.interswitch.services.task.model.Task;
import com.interswitch.services.task.repository.TaskRepository;
import io.swagger.v3.oas.annotations.OpenAPIDefinition;
import io.swagger.v3.oas.annotations.info.Info;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
@OpenAPIDefinition(info =
	@Info(title = "Task API", version = "1.0", description = "Documentation Task API v1.0")
)
public class TaskServiceApplication {

	public static void main(String[] args) {
		SpringApplication.run(TaskServiceApplication.class, args);
	}

	@Bean
	TaskRepository repository(){
		TaskRepository repository = new TaskRepository();
		repository.add(new Task(1L, "Complete Java task", 15L));
		repository.add(new Task(2L, "Assign Alli a new Java task", 25L));
		repository.add(new Task(3L, "Assign Ekeoma a new Java task", 35L));
		return repository;
	}
}
