#include "ui.h"

#include <iostream>

using namespace std;

UI::UI(Controller &ctrl): _ctrl(ctrl) {
    //ctor
}

void UI::showMenu()
{
    cout << "Menu: \n";
    cout << "   1. Add\n";
    cout << "   2. Remove\n";
    cout << "   3. Show all\n";
    cout << "   4. Filter\n";
    cout << "   5. Exit\n";
}

Club getClub(bool readOnlyName = false) {
    string name, type;
    int rating;
    cout << "Name: ";
    cin >> name;
    if(!readOnlyName) {
        cout << "Type: ";
        cin >> type;
        cout << "Rating: ";
        cin >> rating;
    }
    return Club(name, type, rating);
}

void UI::run() {
    while(1) {
        showMenu();
        //cout << "> ";
        int op;
        cin >> op;
        if(op == 1) {
            if(!this->_ctrl.add(getClub()))
                cout << "Already in\n";
            else
                cout << "Success add\n";
        }
        else if(op == 2) {
            if(!this->_ctrl.remove(getClub(1)))
                cout << "No such entry\n";
            else
                cout << "Success remove\n";
        }
        else if(op == 3) {
            for(auto it : this->_ctrl.getAll())
                cout << it.reprHuman() << '\n';
        }
        else if(op == 4) {
            cout << "Filter criteria: ";
            string s;
            cin >> s;
            for(auto it : this->_ctrl.filter(s))
                cout << it.reprHuman() << '\n';
        }
        else if(op == 5) {
            this->_ctrl.save("database.in");
            return ;
        }
    }
}
