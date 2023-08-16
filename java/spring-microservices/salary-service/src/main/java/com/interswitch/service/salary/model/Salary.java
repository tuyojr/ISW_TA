package com.interswitch.service.salary.model;

import java.util.ArrayList;
import java.util.List;

public class Salary {

	private List<Employee> employees = new ArrayList<>();
	private Long employeeId;

	private Long amount;
	private String date;
	private Long departmentId;
	public Salary() {
		
	}

	public Salary(Long employeeId, Long amount, String date) {
		super();
		this.employeeId = employeeId;
		this.amount = amount;
		this.date = date;
	}

	public Long getEmployeeId() {
		return employeeId;
	}

	public void setEmployeeId(Long employeeId) {
		this.employeeId = employeeId;
	}

	public Long getAmount() {
		return amount;
	}

	public void setAmount(Long amount) {
		this.amount = amount;
	}

	public String getDate() {
		return date;
	}

	public void setDate(String date) {
		this.date = date;
	}

	public List<Employee> getEmployees() {
		return employees;
	}

	public void setEmployees(List<Employee> employees) {
		this.employees = employees;
	}

	@Override
	public String toString() {
		return "Salary{" +
				"employeeId=" + employeeId +
				", amount=" + amount +
				", date='" + date + '\'' +
				'}';
	}
}
