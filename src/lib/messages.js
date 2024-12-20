const color= "\x1b[1;35m";
const underline= "\x1b[94;4m";
const normal= "\x1b[0m";
export const introMessage = [
	"+-----------------------------------------------------------------+",
	"|                                                                 |",
	"|   @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @   |",
	"|   @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @   |",
	"|   @ @ @ @ @ @ @ @ @ @                     @ @ @ @ @ @ @ @ @ @   |",
	"|   @ @ @ @ @ @ @ @                             @ @ @ @ @ @ @ @   |",
	"|   @ @ @ @ @ @ @               @ @               @ @ @ @ @ @ @   |",
	"|   @ @ @ @ @ @           @ @ @ @ @ @ @ @           @ @ @ @ @ @   |",
	"|   @ @ @ @ @         @ @ @ @ @ @ @ @ @ @ @ @         @ @ @ @ @   |",
	"|   @ @ @ @         @ @ @ @ @ @ @ @ @   @ @ @ @         @ @ @ @   |",
	"|   @ @ @ @       @ @ @     @ @ @ @         @ @ @       @ @ @ @   |",
	"|   @ @ @         @ @         @ @ @           @ @         @ @ @   |",
	"|   @ @ @       @ @ @         @ @ @ @         @ @ @       @ @ @   |",
	"|   @ @ @       @ @         @ @ @ @ @ @         @ @       @ @ @   |",
	"|   @ @ @       @ @       @ @ @     @ @ @       @ @       @ @ @   |",
	"|   @ @ @     @ @ @       @ @         @ @       @ @ @     @ @ @   |",
	"|   @ @ @ @ @ @ @ @       @ @         @ @       @ @ @     @ @ @   |",
	"|   @ @ @ @ @ @ @ @       @ @ @     @ @ @ @     @ @       @ @ @   |",
	"|   @ @ @ @ @ @ @ @         @ @ @ @ @ @ @ @ @ @ @ @       @ @ @   |",
	"|   @ @ @ @ @ @ @ @ @         @ @ @ @ @ @ @ @ @ @ @       @ @ @   |",
	"|   @ @ @ @ @ @ @ @ @                   @ @ @ @ @         @ @ @   |",
	"|   @ @ @ @ @ @ @ @ @ @                 @ @ @ @ @       @ @ @ @   |",
	"|   @ @ @ @ @ @ @ @ @ @ @ @             @ @ @ @         @ @ @ @   |",
	"|   @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @         @ @ @ @ @   |",
	"|   @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @           @ @ @ @ @ @   |",
	"|   @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @               @ @ @ @ @ @ @   |",
	"|   @ @ @ @ @ @ @ @ @ @ @ @ @ @ @               @ @ @ @ @ @ @ @   |",
	"|   @ @ @ @ @ @ @ @ @ @ @ @ @ @ @           @ @ @ @ @ @ @ @ @ @   |",
	"|   @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @   |",
	"|   @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @   |",
	"|                                                                 |",
	"+-----------------------------------------------------------------+",
	"|                                                                 |",
	"|   Your virtual machine is starting.                             |",
	"|   Please wait while it initializes.                             |",
	"|   This process may take a few seconds to several minutes,       |",
	"|   depending on your internet connection.                        |",
	"|   Everything is ready if you see the prompt: [user@:~/$]        |",
	"|                                                                 |",
	"+-----------------------------------------------------------------+",
	"|                                                                 |",
	"|   You might experience some initial latency in the CLI.         |",
	"|   This is due to the file system being streamed on demand.      |",
	"|   Once a command is executed again, performance will            |",
	"|   approach that of your host machine.                           |",
	"|   Please be patient if you run anything the first time.         |",
	"|                                                                 |",
	"+-----------------------------------------------------------------+",
	"                                                                   "
];
export const errorMessage = [
	color + "CheerpX could not start" + normal,
	"",
	"CheerpX is expected to work with recent desktop versions of Chrome, Edge, Firefox and Safari",
	"",
	"Give it a try from a desktop version / another browser!",
	"",
	"CheerpX internal error message is:",
	""
];
export const unexpectedErrorMessage = [
	color + "WebVM encountered an unexpected error" + normal,
	"",
	"Check the DevTools console for further information",
	"",
	"Please consider reporting a bug!",
	"",
	"CheerpX internal error message is:",
	""
];
