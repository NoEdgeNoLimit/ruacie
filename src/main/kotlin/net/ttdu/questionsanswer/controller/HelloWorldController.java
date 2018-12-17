package net.ttdu.questionsanswer.controller;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

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
        return "index";
    }

    @RequestMapping("/static")
    public String navigatorToStatic() {
        return "redirect:/static.html";
    }
}