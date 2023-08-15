package com.interswitch.service.salary.controller;

import com.interswitch.service.salary.model.Salary;
import com.interswitch.service.salary.repository.SalaryRepository;
import com.interswitch.service.salary.client.EmployeeClient;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class SalaryController {

	private static final Logger LOGGER = LoggerFactory.getLogger(SalaryController.class);

	SalaryRepository repository;
	EmployeeClient employeeClient;

	public SalaryController(SalaryRepository repository, EmployeeClient employeeClient) {
		this.repository = repository;
		this.employeeClient = employeeClient;
	}

	@PostMapping("/")
	public Salary add(@RequestBody Salary salary) {
		LOGGER.info("Salary add: {}", salary);
		return repository.add(salary);
	}
	
//	@GetMapping("/{employeeId}")
//	public Salary findByEmployeeId(@PathVariable("employeeId") Long employeeId) {
//		LOGGER.info("Salary find: employeeId={}", employeeId);
//		return repository.findSalaryByEmployeeId(employeeId);
//	}
	
	@GetMapping("/")
	public List<Salary> findAll() {
		LOGGER.info("Salary find");
		return repository.findAll();
	}
	
	@GetMapping("/salaries/{employeeId}")
	public List<Salary> findByOrganization(@PathVariable("employeeId") Long employeeId) {
		LOGGER.info("Salary find: employeeId={}", employeeId);
		return repository.findSalariesByEmployeeId(employeeId);
	}
	
//	@GetMapping("/salaries/{employeeId}/with-employees")
//	public List<Salary> findByOrganizationWithEmployees(@PathVariable("employeeId") Long employeeId) {
//		LOGGER.info("Salary find: employeeId={}", employeeId);
//		List<Salary> salaries = repository.findSalariesByEmployeeId(employeeId);
//		salaries.forEach(d -> d.setEmployees(employeeClient.findByDepartment(d.getId())));
//		return salaries;
//	}
	
}
