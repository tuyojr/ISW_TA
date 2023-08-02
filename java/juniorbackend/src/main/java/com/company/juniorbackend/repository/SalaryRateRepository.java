package com.company.juniorbackend.repository;

import com.company.juniorbackend.model.SalaryRate;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface SalaryRateRepository extends JpaRepository<SalaryRate, Long> {
}
