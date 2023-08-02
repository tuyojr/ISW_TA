package com.company.juniorbackend.service.impl;

import com.company.juniorbackend.model.Employee;
import com.company.juniorbackend.model.SalaryRate;
import com.company.juniorbackend.repository.SalaryRateRepository;
import com.company.juniorbackend.service.SalaryRateService;

import java.util.List;

public class SalaryRateServiceImpl implements SalaryRateService {
    private final SalaryRateRepository salaryRateRepository;

    public SalaryRateServiceImpl(SalaryRateRepository salaryRateRepository) {
        this.salaryRateRepository = salaryRateRepository;
    }

    @Override
    public SalaryRate createSalaryRate(SalaryRate salaryRate) {
        return salaryRateRepository.save(salaryRate);
    }

    @Override
    public SalaryRate updateSalaryRate(Long rateId, SalaryRate updatedSalaryRate) {
        SalaryRate existingSalaryRate = salaryRateRepository.findById(rateId).orElse(null);
        if (existingSalaryRate != null) {
            existingSalaryRate.setEmployeeCategory(updatedSalaryRate.getEmployeeCategory());
            existingSalaryRate.setLevel(updatedSalaryRate.getLevel());
            existingSalaryRate.setAmount(updatedSalaryRate.getAmount());
            return salaryRateRepository.save(existingSalaryRate);
        }
        return null;
    }

    @Override
    public List<SalaryRate> getAllSalaryRates() {
        return salaryRateRepository.findAll();
    }

    @Override
    public SalaryRate getSalaryRateById(Long rateId) {
        return salaryRateRepository.findById(rateId).orElse(null);
    }
}
