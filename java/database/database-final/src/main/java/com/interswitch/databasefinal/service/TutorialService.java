package com.interswitch.databasefinal.service;

import com.interswitch.databasefinal.model.Tutorial;

import java.util.*;

public interface TutorialService {
    public List<Tutorial> getTutorials();
    public Tutorial addTutorial(Tutorial tutorial);
}
