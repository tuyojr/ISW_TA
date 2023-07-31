package com.interswitch.databasefinal.service;

import com.interswitch.databasefinal.model.Tutorial;
import com.interswitch.databasefinal.repository.TutorialRepository;
import com.interswitch.databasefinal.service.impl.TutorialServiceImpl;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

import static org.assertj.core.api.AssertionsForClassTypes.assertThat;
import static org.mockito.AdditionalAnswers.returnsFirstArg;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

public class TutorialServiceTest {
    private TutorialRepository tutorialRepository;
    private TutorialService tutorialService;

    @BeforeEach
    public void setUp(){
        tutorialRepository = mock(TutorialRepository.class);
        tutorialService = new TutorialServiceImpl(tutorialRepository);
    }

    @Test
    public void testGetTutorials() {
        List<Tutorial> tutorials = new ArrayList<>();
        tutorials.add(new Tutorial(1L, "Book 1", "Title 1", true));
        tutorials.add(new Tutorial(2L, "Book 2", "Title 2", false));
        when(tutorialService.getTutorials()).thenReturn(tutorials);
    }

    @Test
    public void testWhenTutorialIsPublishedReturnTrue(){
        Tutorial tutorial = new Tutorial(1L, "Book 1", "Title 1", true);
        assertThat(tutorial.isPublished()).isTrue();
    }

    @Test
    public void testWhenTutorialAddedReturnID(){
        when(tutorialService.addTutorial(any())).then(returnsFirstArg());
    }

    @Test
    public void testWhenTutorialTitleNotNull(){
        Tutorial tutorial = new Tutorial(1L, "Book 1", "Title 1", true);
        assertThat(tutorial.getTitle()).isNotEmpty();
    }

    @Test
    public void testWhenTutorialAddedReturnTitle(){
        when(tutorialService.addTutorial(any())).then(returnsFirstArg());
    }

    @Test
    public void testWhenTutorialIsNotPublishedReturnFalse(){
        Tutorial tutorial = new Tutorial(1L, "Book 1", "Title 1", false);
        assertThat(tutorial.isPublished()).isFalse();
    }
}
