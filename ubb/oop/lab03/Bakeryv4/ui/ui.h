#ifndef UI_H_INCLUDED
#define UI_H_INCLUDED

#include "../controller/controller.h"
#include "../model/material.h"

typedef enum enum_Commands
{
	CMD_SHOW_OBJECTS			= 1,
	CMD_ADD_OBJECT,
	CMD_DELETE_OBJECT,
	CMD_UPDATE_OBJECT,
	CMD_FILTER_EXPIRED,
	CMD_FILTER_SUPPLIER,
	CMD_FILTER_EMPTYSTOCK,
	CMD_FILTER_WILLEXPIRE,
	CMD_UNDO,
	CMD_REDO,
	MAX_COMMANDS,

	EXIT_CMD 					= 0,
	ERROR_CMD					= -1
}Commands;

typedef struct {
    Controller *ctrl;
} UI;

/// private methods
void ui__printMenu();
int ui__getCmd();
int ui__getInteger(const char *message);
void ui__getString(char *s, const char *message);
Material ui__getMaterial(UI *ui, int, int, int, int);

/// public methods
void run(UI *self);
void ui_init(UI *self, Controller *ctrl);
void ui_destroy(UI *self);

/// commands
void ui_execCMDShowAll(UI *self);
void ui_execCMDAddMaterial(UI *self);
void ui_execCMDDeleteMaterial(UI *self);
void ui_execCMDUpdateMaterial(UI *self);
void ui_execCMDFilterExpired(UI *self);
void ui_execCMDFilterSupplier(UI *self);
void ui_execCMDFilterWillExpire(UI *self);
void ui_execCMDFIlterEmptyStock(UI *self);
void ui_execCMDUndo(UI *self);
void ui_execCMDRedo(UI *self);


#endif // UI_H_INCLUDED
