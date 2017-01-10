package com.company;

import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;

import java.awt.*;
import java.awt.event.MouseEvent;

public class Main extends Application {

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) throws Exception {
        /*
        //Example 1
        Group root = new Group();

        Rectangle r = new Rectangle(25, 25, 50, 50);
        r.setFill(Color.BLUE);
        root.getChildren().add(r);

        Circle c = new Circle(200, 200, 50, Color.web("blue", 0.5f));
        root.getChildren().add(c);
        */
        // Example 2
        HBox root = new HBox(5);
        root.setPadding(new Insets(100));
        root.setAlignment(Pos.BASELINE_RIGHT);

        Button prevBtn = new Button("Previous");
        Button nextBtn = new Button("Next");
        Button cancBtn = new Button("Cancel");
        Button helpBtn = new Button("Help");

        prevBtn.setOnAction(event -> Toolkit.getDefaultToolkit().beep());

        root.getChildren().addAll(prevBtn, nextBtn, cancBtn, helpBtn);
        /*
        // Example 3
        GridPane root = new GridPane();
        root.setPadding(new Insets(20));
        root.setAlignment(Pos.CENTER);

        root.add(new Label("Username: "), 0, 0);
        root.add(new Label("Password: "), 0, 1);

        root.add(new TextField(), 1, 0);
        root.add(new PasswordField(), 1, 1);
        */

        Scene scene = new Scene(root, 1500, 2000, Color.PINK);

        primaryStage.setTitle("Fmm JavaFX!");
        primaryStage.setScene(scene);
        primaryStage.show();
    }
}
