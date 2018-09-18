#include "gui.h"
#include <Exception.h>
#include <qmessagebox.h>
#include <qobject.h>
#include <qwidget.h>
#include <qlistwidget.h>

GUI::GUI(Controller *_c, Programmer _p, QWidget *parent)
	: c(_c), p(_p), QWidget(parent)
{
	ui.setupUi(this);
	QWidget::setWindowTitle(QString::fromStdString(p.getName()));
	connectSignalsAndSlots();
	populateList();
}

GUI::~GUI()
{

}

void GUI::populateList() {
	ui.listTasks->clear();
	for (auto it : c->getTasks()) {
		QString s = QString::fromStdString(it.toListItem());
		if(c->getProgrammer(it.getProg()).getName() != "")
			s += QString::fromStdString("  |  " + c->getProgrammer(it.getProg()).getName());
		ui.listTasks->addItem(new QListWidgetItem(s));
	}
}


void GUI::connectSignalsAndSlots() {
	QObject::connect(ui.buttonAdd, SIGNAL(clicked()), this, SLOT(addTask()));
	QObject::connect(ui.buttonDone, SIGNAL(clicked()), this, SLOT(doDone()));
	QObject::connect(ui.buttonStart, SIGNAL(clicked()), this, SLOT(doStart()));
	QObject::connect(ui.buttonRemove, SIGNAL(clicked()), this, SLOT(removeTask()));
}

void GUI::addTask() {
	///QMessageBox::information(this, "buton", "buton", QMessageBox::Ok, QMessageBox::Ok);
	string act = ui.lineEditDesc->text().toStdString();
	Task t(act, "open", -1);
	c->addTask(t);
}

void GUI::doStart() {
	int ind = getSelectedItem();
	if (ind == -1) {
		QMessageBox::critical(this, "Start Task", "Please select an item from the list in order to start a task!", QMessageBox::Ok, QMessageBox::Ok);
		return;
	}
	Task t = c->getTasks()[ind];
	try {
		c->startTask(t, p);
	} catch(Exception &e) {
		QMessageBox::critical(this, "Start Task", QString(e.what()), QMessageBox::Ok, QMessageBox::Ok);
	}
}

void GUI::doDone() {
	int ind = getSelectedItem();
	if (ind == -1) {
		QMessageBox::critical(this, "Start Task", "Please select an item from the list in order to start a task!", QMessageBox::Ok, QMessageBox::Ok);
		return;
	}
	Task t = c->getTasks()[ind];
	try {
		c->doneTask(t, p);
	}
	catch (Exception &e) {
		QMessageBox::critical(this, "Start Task", QString(e.what()), QMessageBox::Ok, QMessageBox::Ok);
	}
}


int GUI::getSelectedItem() {
	auto v = ui.listTasks->selectedItems();
	if (v.size() == 0)
		return -1;
	return ui.listTasks->row(v[0]);
}

void GUI::removeTask() {
	int ind = getSelectedItem();
	if (ind == -1) {
		QMessageBox::critical(this, "Remove Task", "Please select an item from the list in order to remove a task!", QMessageBox::Ok, QMessageBox::Ok);
		return;
	}
	c->remove(c->getTasks()[ind]);
}