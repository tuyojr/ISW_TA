package com.interswitch.log;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.logging.LogManager;
import java.util.logging.Logger;

public class LoggerTest {

    static Logger LOGGER = Logger.getLogger(LoggerTest.class.getName());

    public static void main(String[] args) throws IOException {
//        LogManager.getLogManager()
//                .readConfiguration(new FileInputStream("mylogging.properties"));


    }
}
