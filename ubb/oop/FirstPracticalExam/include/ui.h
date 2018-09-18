#ifndef UI_H
#define UI_H

#include <controller.h>

class UI
{
    public:
        /** Default constructor */
        UI(Controller &ctrl);
        void showMenu();
        void run();
    private:
        Controller &_ctrl;
};

#endif // UI_H
