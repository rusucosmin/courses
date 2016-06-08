#ifndef GUI_H
#define GUI_H

#include <QtWidgets/QWidget>
#include "ui_gui.h"
#include <Controller.h>
#include <Programmer.h>

class GUI : public QWidget, public Observer
{
	Q_OBJECT

public:
	GUI(Controller *_c, Programmer _p, QWidget *parent = 0);
	~GUI();
	void update() {
		populateList();
	}
public slots:
	void addTask();
	void doStart();
	void doDone();
	void removeTask();
private:
	int getSelectedItem();
	void populateList();
	void connectSignalsAndSlots();
	Ui::GUIClass ui;
	Controller *c;
	Programmer p;
};

#endif // GUI_H
