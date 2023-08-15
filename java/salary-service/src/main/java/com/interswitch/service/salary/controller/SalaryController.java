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
	
	@GetMapping("/{id}")
	public Salary findById(@PathVariable("id") Long id) {
		LOGGER.info("Salary find: id={}", id);
		return repository.findById(id);
	}
	
	@GetMapping("/")
	public List<Salary> findAll() {
		LOGGER.info("Salary find");
		return repository.findAll();
	}
	
	@GetMapping("/organization/{organizationId}")
	public List<Salary> findByOrganization(@PathVariable("organizationId") Long organizationId) {
		LOGGER.info("Salary find: organizationId={}", organizationId);
		return repository.findByOrganization(organizationId);
	}
	
	@GetMapping("/organization/{organizationId}/with-employees")
	public List<Salary> findByOrganizationWithEmployees(@PathVariable("organizationId") Long organizationId) {
		LOGGER.info("Salary find: organizationId={}", organizationId);
		List<Salary> salaries = repository.findByOrganization(organizationId);
		salaries.forEach(d -> d.setEmployees(employeeClient.findByDepartment(d.getId())));
		return salaries;
	}
	
}
