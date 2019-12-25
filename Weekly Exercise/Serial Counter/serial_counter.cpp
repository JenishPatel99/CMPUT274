// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// Name = Jenish Patel
// Student ID: 1572027
// CMPUT 274, FALL 2019
// Weekly Assignment: Serial Monitor
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#include <Arduino.h>

int LEDPIN[5] = { 9, 10, 11, 12, 13 };
uint8_t total = 0;

void setup()
{
    init();

    Serial.begin(9600);

    // Sets output pins
    for (int i = 9; i < 14; i++) {
        pinMode(i, OUTPUT);
    }

    // Prompt
    Serial.println("Enter a number: ");
}

/* 
	Description:
	Processes a char variable and returns the appropriate value.
	Using the ASCII table, each byte is classified and the corresponding
	integer is either return directly (characters 1-9) or processed one 
	more step to return a specific integer (A-F <==> 10-15).

	Arguments:
	digit (char): byte representation of the input in the serial monitor.
*/
int8_t getHexValue(char digit)
{
    int i;

    // Returns integer value which was inputted by user.
    if ((digit >= '0') && (digit <= '9')) {
        for (i = 1; i <= 9; i++) {
            if (char(i + 48) == digit) {
                return i;
            }
        }
    }
    else if ((digit >= 'A') && (digit <= 'F')) {
        for (i = 0; i < 6; i++) {
            if ((char(i + 65) == digit)) {
                return (i + 10);
            }
        }
    }
    else if ((digit >= 'a') && (digit <= 'f')) {
        for (i = 0; i < 6; i++) {
            if ((char(i + 97) == digit)) {
                return (i + 10);
            }
        }
    }
    else if ((digit == char(32)) || (digit == char(13))) {
        return -1;
    }
    else {
        return -2;
    }
}

/*
	Description:
		Using the bitwise operations the uint9_t total quantity is
		traversed from the right most bit to the left and checked
		if bit was 1 or 0. If bit was 1 then the bit position i 
		will be mapped to the LED array and the corresponding LED
		in the array will be turn on, and if bit is 0 the LED will
		be turned off.

	Arguments:
		total (uint8_t) = given input from main.
*/
void update_LED(uint8_t total)
{
    Serial.println(total);
    for (int i = 0; i < 5; i++) {
        if ((total & (1 << i)) != 0) {
            digitalWrite(LEDPIN[i], HIGH);
        }
        else {
            digitalWrite(LEDPIN[i], LOW);
        }
    }
}

int main()
{
    setup();
    char input_char = 0;
    int hex_num;

    while (true) {
        if (Serial.available() > 0) {
            input_char = Serial.read();
            hex_num = getHexValue(input_char);

            // If user presses space or carriage return then total is
            // set to 0.
            if (hex_num == -1) {
                total = 0;
                hex_num = 0;
            }

            // If user presses any forbidden character then a error
            // message will show up.
            if (hex_num == -2) {
                Serial.println("Enter valid HEX key or RESET key");
                hex_num = 0;
            }
            else {
                total += hex_num;
                update_LED(total);
            }
        }
    }
}
