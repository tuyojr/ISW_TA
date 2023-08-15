package com.interswitch.service.salary.repository;

import com.interswitch.service.salary.model.Salary;

import java.util.ArrayList;
import java.util.List;

public class SalaryRepository {

	private final List<Salary> salaries = new ArrayList<>();
	
	public Salary add(Salary salary) {
		salary.setId((long) (salaries.size()+1));
		salaries.add(salary);
		return salary;
	}
	
	public Salary findById(Long id) {
		return salaries.stream()
				.filter(a -> a.getId().equals(id))
				.findFirst()
				.orElseThrow();
	}
	
	public List<Salary> findAll() {
		return salaries;
	}
	
	public List<Salary> findByOrganization(Long organizationId) {
		return salaries.stream()
				.filter(a -> a.getAmount().equals(organizationId))
				.toList();
	}
	
}
