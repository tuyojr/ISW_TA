package com.interswitch.service.salary.model;

import java.util.ArrayList;
import java.util.List;

public class Salary {

	private List<Employee> employees = new ArrayList<>();

	private Long amount;
	private String date;
	private Long id;
	public Salary() {
		
	}

	public Salary(Long amount, String date) {
		super();
		this.amount = amount;
		this.date = date;
	}

	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
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
		return "Salary [id=" + id + ", organizationId=" + amount + ", name=" + date + "]";
	}

}
