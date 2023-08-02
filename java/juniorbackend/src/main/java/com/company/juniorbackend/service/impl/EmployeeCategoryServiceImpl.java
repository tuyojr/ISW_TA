package com.company.juniorbackend.service.impl;

import com.company.juniorbackend.model.EmployeeCategory;
import com.company.juniorbackend.repository.EmployeeCategoryRepository;
import com.company.juniorbackend.service.EmployeeCategoryService;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class EmployeeCategoryServiceImpl implements EmployeeCategoryService {
    private final EmployeeCategoryRepository employeeCategoryRepository;

    public EmployeeCategoryServiceImpl(EmployeeCategoryRepository employeeCategoryRepository) {
        this.employeeCategoryRepository = employeeCategoryRepository;
    }


    @Override
    public EmployeeCategory createEmployeeCategory(EmployeeCategory employeeCategory) {
        return employeeCategoryRepository.save(employeeCategory);
    }

    @Override
    public EmployeeCategory updateEmployeeCategory(Long id, EmployeeCategory employeeCategory) {
        EmployeeCategory existingEmployeeCategory = employeeCategoryRepository.findById(id).orElse(null);
        if (existingEmployeeCategory != null) {
            existingEmployeeCategory.setName(employeeCategory.getName());
            existingEmployeeCategory.setDescription(employeeCategory.getDescription());
            return employeeCategoryRepository.save(existingEmployeeCategory);
        }
        return null;
    }

    @Override
    public List<EmployeeCategory> getAllEmployeeCategories() {
        return employeeCategoryRepository.findAll();
    }

    @Override
    public EmployeeCategory getEmployeeCategoryById(Long id) {
        return employeeCategoryRepository.findById(id).orElse(null);
    }
}
