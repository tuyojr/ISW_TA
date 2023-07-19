package com.interswitch.wallet.application;

import com.interswitch.wallet.application.PageNavigator;

public class RegistrationPage extends PageNavigator {
    @Override
    public String title() {
        return "Registration";
    }

    @Override
    public String instruction() {
        return "Create your wallet account in order to use the application.";
    }

    @Override
    public void setNextPage(PageNavigator nextPage) {
        this.nextPage = nextPage;
    }
}
