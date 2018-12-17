package net.ttdu.questionsanswer

import org.springframework.boot.SpringApplication
import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.web.servlet.support.SpringBootServletInitializer

@SpringBootApplication
class QuestionsAnswerApplication  : SpringBootServletInitializer(){
}
fun main(args: Array<String>) {
	SpringApplication.run(QuestionsAnswerApplication::class.java, *args)
}
