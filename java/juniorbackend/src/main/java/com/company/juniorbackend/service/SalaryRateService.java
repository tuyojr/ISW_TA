package com.company.juniorbackend.service;

import com.company.juniorbackend.model.SalaryRate;
import java.util.*;

public interface SalaryRateService {
    SalaryRate createSalaryRate(SalaryRate salaryRate);
    SalaryRate updateSalaryRate(Long rateId, SalaryRate updatedSalaryRate);
    List<SalaryRate> getAllSalaryRates();
    SalaryRate getSalaryRateById(Long rateId);
}
