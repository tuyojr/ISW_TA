package com.company.juniorbackend.repository;

import com.company.juniorbackend.model.EmployeeCategory;
import org.springframework.data.jpa.repository.JpaRepository;

public interface EmployeeCategoryRepository extends JpaRepository<EmployeeCategory, Long> {
}
