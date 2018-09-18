#ifndef UI_H_INCLUDED
#define UI_H_INCLUDED

typedef struct {
    ;
} UI;

/// private methods
void ui__printMenu();
int ui__getCmd();
int ui__getInteger(const char *message);

/// public methods
void run(UI *self);
void uiInit(UI *self);
void uiDestroy(UI *self);

/// TODO commands


#endif // UI_H_INCLUDED
