package view;

import javafx.application.Application;
import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.ListCell;
import javafx.scene.control.ListView;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.Modality;
import javafx.stage.Stage;
import javafx.util.Callback;
import model.*;
import controller.*;
import repository.*;
import services.PrgStateService;
import sun.security.pkcs11.Secmod;
import view.TextMenu;

import java.io.BufferedReader;
import java.io.IOException;
import java.net.URL;
import java.util.*;

/**
 * Created by cosmin on 10/25/16.
 */
public class Main extends Application {
    public static IRepository getNewRepository(IStmt prg) {
        /// Create the data structures for the program execution
        MyIStack<IStmt> exeStack = new MyStack<>(new Stack<IStmt>());
        MyIDictionary<String, Integer> symTable = new MyDictionary<>(new HashMap<String, Integer>());
        MyIList<Integer> out = new MyList<>(new ArrayList<Integer>());
        MyIDictionary<Integer, Tuple<String, BufferedReader>> fileTable = new MyDictionary<>(new HashMap<Integer, Tuple<String, BufferedReader>>());
        MyIHeap<Integer> heap = new MyHeap<Integer>(new HashMap<Integer, Integer>());

        PrgState prgState = new PrgState(exeStack, symTable, out, prg, fileTable, heap, 1);
        IRepository repo = new Repository(prgState, "log.txt");
        return repo;
    }
    public static void main(String [] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) throws Exception {
        /*
        *   Lab2Ex1:
        *   v = 2;
        *   print (v)
        *
        * */
        IStmt lab2ex1= new CompStmt(new AssignStmt("v",new ConstExp(2)), new PrintStmt(new
                VarExp("v")));
        /*
        *   Lab2Ex2:
        *   a = 2 + 3 * 5;
        *   b = a + 1;
        *   print (b)
        *
        * */
        IStmt lab2ex2 = new CompStmt(new AssignStmt("a", new ArithExp('+',new ConstExp(2),new
                ArithExp('*',new ConstExp(3), new ConstExp(5)))),
                new CompStmt(new AssignStmt("b",new ArithExp('+',new VarExp("a"), new
                        ConstExp(1))), new PrintStmt(new VarExp("b"))));
        /*
        *   Lab2Ex3:
        *   a = 2 - 2;
        *   If a then v = 2 else v = 3;
        *   print (v)
        *
        * */
        IStmt lab2ex3 = new CompStmt(new AssignStmt("a", new ArithExp('-',new ConstExp(2), new
                ConstExp(2))),
                new CompStmt(new IfStmt(new VarExp("a"),new AssignStmt("v",new ConstExp(2)), new
                        AssignStmt("v", new ConstExp(3))), new PrintStmt(new VarExp("v"))));


        /*
        *   Lab5Ex1
        *   openRFile (var_f, "test.in");
        *   readFile (var_f, var_c); print (var_c);
        *   If var_c then readFile (var_f, var_c); print (var_c) else print (0);
        *   closeRFile (var_f)
        *
        * */
        IStmt lab5ex1 = new CompStmt(
                new OpenRFileStmt("var_f", "test.in"),
                new CompStmt(
                        new ReadFileStmt(new VarExp("var_f"), "var_c"),
                        new CompStmt(
                                new PrintStmt(new VarExp("var_c")),
                                new CompStmt(
                                        new IfStmt(
                                                new VarExp("var_c"),
                                                new CompStmt(
                                                    new ReadFileStmt(new VarExp("var_f"), "var_c"),
                                                    new PrintStmt(new VarExp("var_c"))
                                                ),
                                                new PrintStmt(new ConstExp(0))
                                        ),
                                        new CloseRFileStmt(new VarExp("var_f"))
                                )
                        )
                )
        );

        /*
        *   Lab5Ex2
        *   openRFile (var_f, "test.in");
        *   readFile (var_f + 2, var_c); print (var_c);
        *   If var_c then readFile (var_f, var_c); print (var_c) else print (0);
        *   closeRFile (var_f)
        * */
        IStmt lab5ex2 = new CompStmt(
                new OpenRFileStmt("var_f", "test.in"),
                new CompStmt(
                        new ReadFileStmt(new ArithExp('+', new VarExp("var_f"), new ConstExp(2)), "var_c"),
                        new CompStmt(
                                new PrintStmt(new VarExp("var_c")),
                                new CompStmt(
                                        new IfStmt(
                                                new VarExp("var_c"),
                                                new CompStmt(
                                                    new ReadFileStmt(new VarExp("var_f"), "var_c"),
                                                    new PrintStmt(new VarExp("var_c"))
                                                ),
                                                new PrintStmt(new ConstExp(0))
                                        ),
                                        new CloseRFileStmt(new VarExp("var_f"))
                                )
                        )
                )
        );
        /**
         *v=10;new(v,20);new(a,22);wH(a,30);print(a);print(rH(a));a=0
         *
         * */
        IStmt lab6ex1 =
        new CompStmt(
                new AssignStmt("v", new ConstExp(10)),
                new CompStmt(
                    new NewStmt("v", new ConstExp(20)),
                        new CompStmt(
                            new NewStmt("a", new ConstExp(22)),
                            new CompStmt(
                                new WriteHeapStmt("a", new ConstExp(30)),
                                new CompStmt(
                                    new PrintStmt(new VarExp("a")),
                                    new CompStmt(
                                            new PrintStmt(new ReadHeapExp("a")),
                                            new AssignStmt("a", new ConstExp(0)))))
                        )
                )
        );
        IStmt lab7test = new CompStmt(
            new AssignStmt("v", new ConstExp(0)),
                new WhileStmt(new CompExp("<=", new VarExp("v"), new ConstExp(10)),
                        new CompStmt(
                                new PrintStmt(new VarExp("v")),
                                new AssignStmt("v", new ArithExp('+', new VarExp("v"), new ConstExp(1)))
                                ))
        );
        IStmt lab7ex1 = new CompStmt(
            new AssignStmt("v", new ConstExp(6)),
                new CompStmt(
                    new WhileStmt(new ArithExp('-', new VarExp("v"), new ConstExp(4)),
                            new CompStmt(
                                    new PrintStmt(new VarExp("v")),
                                    new AssignStmt("v", new ArithExp('-', new VarExp("v"), new ConstExp(1)))
                                    )),
                        new PrintStmt(new VarExp("v")))
        );
//        v=6; (while (v-4) print(v);v=v-1);print(v)
        /*
            v=10;new(a,22);
            fork(wH(a,30);v=32;print(v);print(rH(a)));
            print(v);print(rH(a))
        */
        IStmt lab8ex1 = new CompStmt(
                new CompStmt(
                    new AssignStmt("v", new ConstExp(10)),
                    new NewStmt("a", new ConstExp(22))
                ),
                new CompStmt(
                        new ForkStmt(
                                new CompStmt(
                                    new WriteHeapStmt("a", new ConstExp(30)),
                                        new CompStmt(
                                                new AssignStmt("v", new ConstExp(32)),
                                                new CompStmt(
                                                        new PrintStmt(new VarExp("v")),
                                                        new PrintStmt(new ReadHeapExp("a"))
                                                )
                                        )
                                )
                        ),
                        new CompStmt(
                                new PrintStmt(new VarExp("v")),
                                new PrintStmt(new ReadHeapExp("a"))
                        )
                )
        );
        ///create the list of istmts
        List<IStmt> menu = new ArrayList<IStmt>();
        menu.add(lab2ex1);
        menu.add(lab2ex2);
        menu.add(lab2ex3);
        menu.add(lab5ex1);
        menu.add(lab5ex2);
        menu.add(lab6ex1);
        menu.add(lab7test);
        menu.add(lab7ex1);
        menu.add(lab8ex1);

        VBox root = new VBox(5);
        root.getChildren().add(new Label("Plase choose a program: "));

        /// create the listview
        ObservableList<IStmt> observableStmtList = FXCollections.observableArrayList(menu);
        ListView<IStmt> programList = new ListView<IStmt>(observableStmtList);
        programList.setCellFactory(new Callback<ListView<IStmt>, ListCell<IStmt>>() {
            @Override
            public ListCell<IStmt> call(ListView<IStmt> param) {
                ListCell<IStmt> listCell = new ListCell<IStmt>() {
                    @Override
                    protected void updateItem(IStmt e, boolean empty) {
                        super.updateItem(e, empty);
                        if(e == null || empty)
                            setText("");
                        else
                            setText(e.toString());
                    }
                };
                return listCell;
            }
        });
        root.getChildren().add(programList);

        Scene scene = new Scene(root, 100, 100);

        primaryStage.setScene(scene);
        primaryStage.setTitle("Examples");
        primaryStage.show();

        observableStmtList.add(new PrintStmt(new ConstExp(1)));

        programList.getSelectionModel().selectedItemProperty().addListener(new ChangeListener<IStmt>() {
            @Override
            public void changed(ObservableValue<? extends IStmt> observable, IStmt oldValue, IStmt newValue) {
                try {
                    FXMLLoader loader = new FXMLLoader();
                    loader.setLocation(Main.class.getResource("RunProgram.fxml"));
                    VBox root = (VBox) loader.load();

                    PrgStateService prgStateService = new PrgStateService(getNewRepository(newValue));
                    Controller ctrl = loader.getController();
                    ctrl.setService(prgStateService);
                    prgStateService.addObserver(ctrl);

                    Stage dialogStage = new Stage();
                    dialogStage.setTitle("Run example dialog");
                    dialogStage.initModality(Modality.APPLICATION_MODAL);
                    dialogStage.setScene(new Scene(root));
                    dialogStage.show();
                } catch(IOException e) {
                    e.printStackTrace();
                }
                /*
                Stage dialogStage = new Stage();
                dialogStage.setTitle("Run example dialog");
                dialogStage.initModality(Modality.APPLICATION_MODAL);
                dialogStage.setScene(new Scene(new Label(newValue.getDescription())));
                dialogStage.show();
                */
            }
        });
    }
}
