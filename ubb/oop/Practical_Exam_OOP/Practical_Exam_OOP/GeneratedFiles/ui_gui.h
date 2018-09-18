/********************************************************************************
** Form generated from reading UI file 'gui.ui'
**
** Created by: Qt User Interface Compiler version 5.6.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_GUI_H
#define UI_GUI_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_GUIClass
{
public:
    QVBoxLayout *verticalLayout_2;
    QVBoxLayout *verticalLayout;
    QListWidget *listTasks;
    QGridLayout *gridLayout;
    QLabel *labelAdd;
    QPushButton *buttonAdd;
    QLineEdit *lineEditDesc;
    QPushButton *buttonRemove;
    QPushButton *buttonStart;
    QPushButton *buttonDone;

    void setupUi(QWidget *GUIClass)
    {
        if (GUIClass->objectName().isEmpty())
            GUIClass->setObjectName(QStringLiteral("GUIClass"));
        GUIClass->resize(600, 400);
        verticalLayout_2 = new QVBoxLayout(GUIClass);
        verticalLayout_2->setSpacing(6);
        verticalLayout_2->setContentsMargins(11, 11, 11, 11);
        verticalLayout_2->setObjectName(QStringLiteral("verticalLayout_2"));
        verticalLayout = new QVBoxLayout();
        verticalLayout->setSpacing(6);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        listTasks = new QListWidget(GUIClass);
        listTasks->setObjectName(QStringLiteral("listTasks"));

        verticalLayout->addWidget(listTasks);

        gridLayout = new QGridLayout();
        gridLayout->setSpacing(6);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        labelAdd = new QLabel(GUIClass);
        labelAdd->setObjectName(QStringLiteral("labelAdd"));

        gridLayout->addWidget(labelAdd, 1, 0, 1, 1);

        buttonAdd = new QPushButton(GUIClass);
        buttonAdd->setObjectName(QStringLiteral("buttonAdd"));

        gridLayout->addWidget(buttonAdd, 1, 3, 1, 1);

        lineEditDesc = new QLineEdit(GUIClass);
        lineEditDesc->setObjectName(QStringLiteral("lineEditDesc"));

        gridLayout->addWidget(lineEditDesc, 1, 2, 1, 1);

        buttonRemove = new QPushButton(GUIClass);
        buttonRemove->setObjectName(QStringLiteral("buttonRemove"));

        gridLayout->addWidget(buttonRemove, 2, 3, 1, 1);

        buttonStart = new QPushButton(GUIClass);
        buttonStart->setObjectName(QStringLiteral("buttonStart"));

        gridLayout->addWidget(buttonStart, 2, 0, 1, 1);

        buttonDone = new QPushButton(GUIClass);
        buttonDone->setObjectName(QStringLiteral("buttonDone"));

        gridLayout->addWidget(buttonDone, 2, 2, 1, 1);


        verticalLayout->addLayout(gridLayout);


        verticalLayout_2->addLayout(verticalLayout);


        retranslateUi(GUIClass);

        QMetaObject::connectSlotsByName(GUIClass);
    } // setupUi

    void retranslateUi(QWidget *GUIClass)
    {
        GUIClass->setWindowTitle(QApplication::translate("GUIClass", "GUI", 0));
        labelAdd->setText(QApplication::translate("GUIClass", "Description: ", 0));
        buttonAdd->setText(QApplication::translate("GUIClass", "Add", 0));
        buttonRemove->setText(QApplication::translate("GUIClass", "Remove", 0));
        buttonStart->setText(QApplication::translate("GUIClass", "Start", 0));
        buttonDone->setText(QApplication::translate("GUIClass", "Done", 0));
    } // retranslateUi

};

namespace Ui {
    class GUIClass: public Ui_GUIClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_GUI_H
