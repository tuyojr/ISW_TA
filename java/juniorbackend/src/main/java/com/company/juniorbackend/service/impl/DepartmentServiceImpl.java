package com.company.juniorbackend.service.impl;

import com.company.juniorbackend.model.Department;
import com.company.juniorbackend.repository.DepartmentRepository;
import com.company.juniorbackend.service.DepartmentService;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class DepartmentServiceImpl implements DepartmentService {
    private final DepartmentRepository departmentRepository;

    public DepartmentServiceImpl(DepartmentRepository departmentRepository) {
        this.departmentRepository = departmentRepository;
    }

    @Override
    public Department createDepartment(Department department) {
        return departmentRepository.save(department);
    }

    @Override
    public Department updateDepartment(Long departmentId, Department department) {
        Department existingDepartment = departmentRepository.findById(departmentId).orElse(null);
        if(existingDepartment != null){
            existingDepartment.setName(department.getName());
            existingDepartment.setDescription(department.getDescription());
            return departmentRepository.save(existingDepartment);
        }
        return null;
    }

    @Override
    public List<Department> getAllDepartments() {
        return departmentRepository.findAll();
    }

    @Override
    public Department getDepartmentById(Long departmentId) {
        return departmentRepository.findById(departmentId).orElse(null);
    }
}
