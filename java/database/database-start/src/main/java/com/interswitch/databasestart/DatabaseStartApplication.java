package com.interswitch.databasestart;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/* STEPS FOR CREATING REST API WITH SPRINGBOOT
SETUP THE DEVELOPMENT ENVIRONMENT: JDK, INTELLIJ, DATABASE
USING START.SPRING.IO, GENERATE A SPRINGBOOT PROJECT AND IT'S DEPENDENCIES
CREATE ENTITY CLASS: USING THE REQUIRED ANNOTATIONS @Entity @Table @Id @Column etc
CREATE REPOSITORY INTERFACE: EXTENDS JPA REPOSITORY
CREATE SERVICE INTERFACE: DEFINE THE REQUIRED METHODS
CREATE THE SERVICE IMPLEMENTATION CLASS: IMPLEMENT THE REQUIRED METHODS AND AUTOWIRE THE REPOSITORY INTERFACE
CREATE THE CONTROLLER CLASS: DEFINE THE REQUIRED ENDPOINTS AND AUTOWIRE THE SERVICE INTERFACE
* */
@SpringBootApplication
public class DatabaseStartApplication {

	public static void main(String[] args) {
		SpringApplication.run(DatabaseStartApplication.class, args);
	}

}
