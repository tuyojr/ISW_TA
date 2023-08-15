package com.interswitch.service.salary.repository;

import com.interswitch.service.salary.model.Salary;

import java.util.ArrayList;
import java.util.List;

public class SalaryRepository {

	private List<Salary> salaries = new ArrayList<>();
	
	public Salary add(Salary salary) {
//		salary.setId((long) (salaries.size()+1));
		salaries.add(salary);
		return salary;
	}
	
	public Salary findSalaryByEmployeeId(Long employeeId) {
		return salaries.stream()
				.filter(a -> a.getEmployeeId().equals(employeeId))
				.findFirst()
				.orElseThrow();
	}
	
	public List<Salary> findAll() {
		return salaries;
	}
	
	public List<Salary> findSalariesByEmployeeId(Long employeeId) {
		return salaries.stream()
				.filter(a -> a.getEmployeeId().equals(employeeId))
				.toList();
	}
	
}
