package com.interswitch.ajax.assessment;

import org.json.JSONObject;

public class JSONTest {
    public static void main(String[] args) {
        JSONObject jo = new JSONObject();
        jo.put("name", "Hidan");
        jo.put("age", 28);
        jo.put("isTall", true);
        String js = jo.toString();
        System.out.println(jo);

        JSONObject jo2 = new JSONObject(
                "{\"name\": \"Alice\", " +
                        "\"age\": 30, " +
                        "\"city\": \"New York\"}"
        );
        System.out.println(jo2);
    }
}
