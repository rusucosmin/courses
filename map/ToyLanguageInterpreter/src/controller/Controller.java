package controller;

import exception.*;
import javafx.beans.property.SimpleStringProperty;
import javafx.beans.value.ObservableValue;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.util.Callback;
import model.*;
import repository.IRepository;
import services.PrgStateService;
import utils.Observable;

import java.io.IOException;
import java.util.Collection;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.stream.Collector;
import java.util.stream.Collectors;

/**
 * Created by cosmin on 10/25/16.
 */
public class Controller implements utils.Observer<PrgState> {
    @FXML
    private Label prgStatesCnt;
    @FXML
    private TableView<Map.Entry<Integer, Integer>> heapTableView;
    @FXML
    private ListView<String> outListView;
    @FXML
    private TableView<Tuple<Integer, String>> fileTableView;
    @FXML
    private ListView<PrgState> prgStateListView;
    @FXML
    private Label prgIdLabel;
    @FXML
    private ListView exeStackListView;

    private IRepository rep;
    ObservableList<PrgState> prgStateModel;
    ObservableList<String> outListModel;
    ObservableList<Map.Entry<Integer, Integer>> heapTableModel;
    ObservableList<Tuple<Integer, String>> fileTableModel;
    private ExecutorService executor;
    private PrgStateService prgStateService;

    public Controller() {
    }

    @FXML
    private void initialize() {
    }

    public void setService(PrgStateService prgStateService) {
        this.prgStateService = prgStateService;
        this.rep = this.prgStateService.getRepo();
        //prg state model;
        this.prgStateModel = FXCollections.observableArrayList();
        this.prgStateListView.setItems(this.prgStateModel);
        this.prgStateListView.setCellFactory(new Callback<ListView<PrgState>, ListCell<PrgState>>() {
            @Override
            public ListCell<PrgState> call(ListView<PrgState> param) {
                ListCell<PrgState> listCell = new ListCell<PrgState>() {
                    @Override
                    protected void updateItem(PrgState e, boolean empty) {
                        super.updateItem(e, empty);
                        if(e == null || empty)
                            setText("");
                        else
                            setText(String.valueOf(e.getId()));
                    }
                };
                return listCell;
            }
        });
        // heapTableView
        this.heapTableModel = FXCollections.observableArrayList();
        TableColumn<Map.Entry<Integer, Integer>, String> first = new TableColumn<>("Address");
        TableColumn<Map.Entry<Integer, Integer>, String> second = new TableColumn<>("Value");
        first.setCellValueFactory(new Callback<TableColumn.CellDataFeatures<Map.Entry<Integer, Integer>, String>, ObservableValue<String>>() {
            @Override
            public ObservableValue<String> call(TableColumn.CellDataFeatures<Map.Entry<Integer, Integer>, String> param) {
                return new SimpleStringProperty(String.valueOf(param.getValue().getKey()));
            }
        });
        second.setCellValueFactory(new Callback<TableColumn.CellDataFeatures<Map.Entry<Integer, Integer>, String>, ObservableValue<String>>() {
            @Override
            public ObservableValue<String> call(TableColumn.CellDataFeatures<Map.Entry<Integer, Integer>, String> param) {
                return new SimpleStringProperty(String.valueOf(param.getValue().getValue()));
            }
        });
        this.heapTableView.getColumns().setAll(first, second);
        this.heapTableView.setItems(this.heapTableModel);

        ///fileTableView
        this.fileTableModel = FXCollections.observableArrayList();
        TableColumn<Tuple<Integer, String>, String> fd = new TableColumn<>("File descriptor");
        TableColumn<Tuple<Integer, String>, String> fn = new TableColumn<>("File name");
        fd.setCellValueFactory(new Callback<TableColumn.CellDataFeatures<Tuple<Integer, String>, String>, ObservableValue<String>>() {
            @Override
            public ObservableValue<String> call(TableColumn.CellDataFeatures<Tuple<Integer, String>, String> param) {
                return new SimpleStringProperty(String.valueOf(param.getValue().getFirst()));
            }
        });
        fn.setCellValueFactory(new Callback<TableColumn.CellDataFeatures<Tuple<Integer, String>, String>, ObservableValue<String>>() {
            @Override
            public ObservableValue<String> call(TableColumn.CellDataFeatures<Tuple<Integer, String>, String> param) {
                return new SimpleStringProperty(String.valueOf(param.getValue().getSecond()));
            }
        });
        this.fileTableView.getColumns().setAll(fd, fn);
        this.fileTableView.setItems(this.fileTableModel);

        // outListView
        this.outListModel = FXCollections.observableArrayList();
        this.outListView.setItems(this.outListModel);

        this.update(this.prgStateService);
    }

    Map<Integer, Integer> conservativeGarbageCollector(Collection<Integer> symTableValues, Map<Integer, Integer> heap) {
        return heap.entrySet()
                .stream()
                .filter(e->symTableValues.contains(e.getKey()))
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
    }

    public List<PrgState> removeCompletedPrg(List<PrgState> prgStateList) {
        return prgStateList.stream()
                .filter(p -> p.isNotCompleted())
                .collect(Collectors.toList());
    }

    public void setMain(PrgState state) {
        this.rep.getPrgList().clear();
        this.rep.getPrgList().add(state);
    }

    public void serialize() {
        this.rep.serialize();
    }

    public void deserializa() {
        this.rep.deserialize();
    }

    public void oneStepForAllPrg(List<PrgState> prgList) throws InterruptedException {
        /// Log the states before the execution
        prgList.forEach(prg -> {
            try {
                rep.logPrgStateExec(prg);
            } catch (IOException e) {
                e.printStackTrace();
            }
        });

        List<Callable<PrgState>> callList = prgList.stream()
                .map((PrgState p) -> (Callable<PrgState>)(() -> {return p.oneStep();}))
                .collect(Collectors.toList());

        List<PrgState> newPrgList = executor.invokeAll(callList).stream()
                .map(future -> {
                    try {
                        return future.get();
                    } catch (Exception e) {
                        System.out.println(e);
                    }
                    return null;
                })
                .filter(p -> p != null)
                .collect(Collectors.toList());

        prgList.addAll(newPrgList);
        prgList.forEach(prg -> {
            try {
                rep.logPrgStateExec(prg);
            } catch (IOException e) {
                e.printStackTrace();
            }
        });

        rep.setPrgList(prgList);
        this.prgStateService.notifyObservers();
    }



    public void allSteps() throws UnknownVariableException, DivideByZeroException, FileAlreadyOpenedException, FileNotOpenedException, IOException, UnknownComparisonExpression, InterruptedException {
        executor = Executors.newFixedThreadPool(2);
        while(true) {
            List<PrgState> prgList = removeCompletedPrg(this.prgStateService.getAll());
            if(prgList.size() == 0)
                break;
            oneStepForAllPrg(prgList);
        }
        executor.shutdownNow();
        /*
        List<PrgState> prgList = rep.getPrgList();
        while(!crt.getExeStack().isEmpty()) {
            //this.rep.serialize();
            oneStep(crt);
            crt.getHeap().setMap(this.conservativeGarbageCollector(crt.getSymTable().values(), crt.getHeap().getMap()));
            //this.rep.deserialize();
            try {
                rep.logPrgStateExec();
            } catch (IOException e) {
                System.out.println("Cannot log program state to file. Exiting...");
                return ;
            }
        }
        */
    }


    @FXML
    public void allStepsGUI() throws UnknownVariableException, DivideByZeroException, FileAlreadyOpenedException, FileNotOpenedException, IOException, UnknownComparisonExpression, InterruptedException {
        executor = Executors.newFixedThreadPool(2);
        while(true) {
            this.prgStateService.notifyObservers();
            List<PrgState> prgList = removeCompletedPrg(this.prgStateService.getAll());
            if(prgList.size() == 0) {
                System.out.println("FINISHED");
                break;
            }
            oneStepForAllPrg(prgList);
            System.out.println("ONE STEP");
            break;
        }
        executor.shutdownNow();
        /*
        List<PrgState> prgList = rep.getPrgList();
        while(!crt.getExeStack().isEmpty()) {
            //this.rep.serialize();
            oneStep(crt);
            crt.getHeap().setMap(this.conservativeGarbageCollector(crt.getSymTable().values(), crt.getHeap().getMap()));
            //this.rep.deserialize();
            try {
                rep.logPrgStateExec();
            } catch (IOException e) {
                System.out.println("Cannot log program state to file. Exiting...");
                return ;
            }
        }
        */
    }

    @Override
    public void update(Observable<PrgState> observable) {
        List<PrgState> prgStates = this.prgStateService.getAll();
        this.prgStatesCnt.setText(String.valueOf(prgStates.size()));
        this.prgStateModel.setAll(prgStates);
        this.outListModel.setAll(this.prgStateService.getOutList());
        this.heapTableModel.setAll(this.prgStateService.getHeapList());
        this.fileTableModel.setAll(prgStates.get(0).getFileTable().keys()
                .stream()
                .map(k -> new Tuple<Integer, String>(k, prgStates.get(0).getFileTable().get(k).getFirst()))
                .collect(Collectors.toList())
        );
        this.fileTableModel.stream().map(e->String.valueOf(e.getFirst()) + e.getSecond()).forEach(System.out::println);
    }
}
