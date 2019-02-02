package net.ttdu.questionsanswer.controller;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;
import java.util.ArrayList;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.google.cloud.datastore.Datastore;
import com.google.cloud.datastore.DatastoreOptions;
import com.google.cloud.datastore.Entity;
import com.google.cloud.datastore.Key;
import com.google.cloud.datastore.KeyFactory;
/**
 * @Author: jiyuhui
 * @Date: 2018/12/13
 * @Version 1.0
 * @describe
 */
@Controller
public class HelloWorldController {
    @Value("${user.ok}")
    private String name;

    @RequestMapping("/hello")
    public String index() {
        return "Hello World";
    }
    @GetMapping("/")
    public String homePage(Model model, HttpServletRequest request, HttpServletResponse response) throws IOException {
        model.addAttribute("name", name);


        request.getContextPath();
        new ArrayList<>();
        return "index";
    }

    @RequestMapping("/static")
    public String navigatorToStatic() {
        return "redirect:/static.html";
    }
    @RequestMapping("/data")
    public String datatest(){
        // Instantiates a client
        Datastore datastore = DatastoreOptions.getDefaultInstance().getService();

        // The kind for the new entity
        String kind = "Task";
        // The name/ID for the new entity
        String name = "sampletask1";
        // The Cloud Datastore key for the new entity
        Key taskKey = datastore.newKeyFactory().setKind(kind).newKey(name);

        // Prepares the new entity
        Entity task = Entity.newBuilder(taskKey)
                .set("description", "Buy milk")
                .build();

        // Saves the entity
        datastore.put(task);

        System.out.printf("Saved %s: %s%n", task.getKey().getName(), task.getString("description"));

        //Retrieve entity
        Entity retrieved = datastore.get(taskKey);

        System.out.printf("Retrieved %s: %s%n", taskKey.getName(), retrieved.getString("description"));

        return null;
    }
}