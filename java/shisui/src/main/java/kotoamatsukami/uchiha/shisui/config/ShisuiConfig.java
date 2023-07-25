package kotoamatsukami.uchiha.shisui.config;

import kotoamatsukami.uchiha.shisui.greet.Greet;
import kotoamatsukami.uchiha.shisui.greet.implementation.Greeting;
import kotoamatsukami.uchiha.shisui.greet.implementation.NewDay;
import kotoamatsukami.uchiha.shisui.greet.implementation.Night;
import org.springframework.boot.autoconfigure.condition.ConditionalOnProperty;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class ShisuiConfig {

    @Bean(name="wetinDeySup", initMethod="whoGoes", destroyMethod="clearRoad")
    public Greeting wetinDeySup(){
        return new Greeting();
    }

    @ConditionalOnProperty(name="time_of_day", havingValue="noon", matchIfMissing=true)

    @Bean
    public Greet newDay(){
        return new NewDay();
    }

    @ConditionalOnProperty(name="time_of_day", havingValue="night", matchIfMissing=false)

    @Bean
    public Greet night(){
        return new Night();
    }
}
