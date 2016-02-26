#ifndef UI_H_INCLUDED
#define UI_H_INCLUDED

typedef enum enum_Commands
{
	CMD_SHOW_OBJECTS			= 1,
	CMD_ADD_OBJECT,
	CMD_DELETE_OBJECT,
	CMD_UPDATE_OBJECT,
	MAX_COMMANDS,

	EXIT_CMD 					= 0,
	ERROR_CMD					= -1
}Commands;

typedef struct {
    ;
} UI;

/// private methods
void ui__printMenu();
int ui__getCmd();
int ui__getInteger(const char *message);

/// public methods
void run(UI *self);
void ui_init(UI *self);
void ui_destroy(UI *self);

/// commands
void ui_execCMDShowAll(UI *self);
void ui_execCMDAddMaterial(UI *self);
void ui_execCMDDeleteMaterial(UI *self);
void ui_execCMDUpdateMaterial(UI *self);

#endif // UI_H_INCLUDED
