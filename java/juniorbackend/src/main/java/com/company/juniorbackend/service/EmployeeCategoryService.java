package com.company.juniorbackend.service;

import com.company.juniorbackend.model.EmployeeCategory;
import java.util.List;

public interface EmployeeCategoryService {
    EmployeeCategory createEmployeeCategory(EmployeeCategory employeeCategory);
    EmployeeCategory updateEmployeeCategory(Long id, EmployeeCategory employeeCategory);
    List<EmployeeCategory> getAllEmployeeCategories();
    EmployeeCategory getEmployeeCategoryById(Long id);
}
