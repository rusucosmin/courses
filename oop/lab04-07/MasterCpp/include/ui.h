#include <controller.h>
#include <tutorial.h>

#ifndef UI_H
#define UI_H


class UI {
    public:
        /** Default constructor */
        UI(Controller &ctrl);
        void run();

    private:
        Controller &_ctrl;
        void _show_admin_menu();
        void _run_user();
        void _run_admin();
        void _admin_add_tutorial();
        void _admin_remove_tutorial();
        void _admin_update_tutorial();
        void _admin_show_all();
        string _read_string(string msg);
        int _read_int(string msg);
        Tutorial _read_tutorial(bool, bool, bool, bool, bool);
};

#endif // UI_H
