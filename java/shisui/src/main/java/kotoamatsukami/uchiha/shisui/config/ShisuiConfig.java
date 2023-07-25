package kotoamatsukami.uchiha.shisui.config;

import kotoamatsukami.uchiha.shisui.greet.Greeting;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class ShisuiConfig {

    @Bean(name="wetinDeySup", initMethod="whoGoes", destroyMethod="clearRoad")
    public Greeting wetinDeySup(){
        return new Greeting();
    }
}
