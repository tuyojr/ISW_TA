package com.interswitch.ajax.json;

import org.json.JSONArray;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class JsonTest {
    public static void main(String[] args) {
        JSONObject jo = new JSONObject();
        jo.put("name", "Hidan");
        jo.put("age", 28);
        jo.put("isTall", true);
        System.out.println(jo);

        Map<String, String> map = new HashMap<>();
        map.put("name", "Lionel");
        map.put("age", "35");
        map.put("city", "Barcelona");
        JSONObject jo1 = new JSONObject(map);
        System.out.println(map);
        System.out.println(jo1);

        JSONObject jo2 = new JSONObject(
                "{\"name\":\"Kakuzu\"," +
                        "\"age\":375," +
                        "\"isImmortal\":true}"
        );
        System.out.println(jo2);

        DemoBean demoBean = new DemoBean();
        demoBean.setId(25L);
        demoBean.setName("Madara");
        demoBean.setActive(true);

        JSONObject jo3 = new JSONObject(demoBean);
        System.out.println(jo3);

        JSONArray ja = new JSONArray();
        ja.put(Boolean.TRUE);
        ja.put("Madara");

        JSONObject jo4 = new JSONObject();
        jo4.put("name", "Kisame");
        jo4.put("age", 32);
        jo4.put("sword", "Samehada");
        ja.put(jo4);

        JSONObject jo5 = new JSONObject();
        jo5.put("name", "Itachi");
        jo5.put("age", 28);
        jo5.put("powerUp", "Tsukuyomi");
        ja.put(jo5);

        JSONObject jo6 = new JSONObject();
        jo6.put("name", "Kakashi");
        jo6.put("age", 32);
        jo6.put("powerUp", "Kamui");
        ja.put(jo6);
        System.out.println(ja);

        JSONArray ja1 = new JSONArray("[Infinite Tsukuyomi, \"Uchiha Obito\", 29]");
        System.out.println(ja1);

        List<String> list = new ArrayList<>();
        list.add("Team 7");
        list.add("Kakashi");
        list.add("Naruto");
        list.add("Sasuke");
        list.add("Sakura");
        JSONArray ja2 = new JSONArray(list);

        System.out.println(ja2);
    }
}
