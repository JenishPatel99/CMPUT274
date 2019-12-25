// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// Name = Jenish Patel
// Student ID: 1572027
// CMPUT 274, FALL 2019
// Weekly Assignment: Counting Lights
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#include <Arduino.h>

// Constants and Variable
const int LEDPIN[5] = { 9, 10, 11, 12, 13 };
int LED[5] = { LOW, LOW, LOW, LOW, LOW};
const int inc_button = 6;
const int dec_button = 7;
const int store_button = 5;

void setup()
{
    init();
    Serial.begin(9600);

    // Sets pin mode for LEDs
    for (int i = 9; i < 14; i++) {
        pinMode(i, OUTPUT);
    }

    // Sets push button inputs and pull up resistor
    pinMode(inc_button, INPUT);
    digitalWrite(inc_button, HIGH);
    pinMode(dec_button, INPUT);
    digitalWrite(dec_button, HIGH);
    pinMode(store_button, INPUT);
    digitalWrite(store_button, HIGH);
}

/* 
	Description: 
		Converts decimal number to binary and maps it to the
		LED array. The current state of the LED is stored in
		the array and displayed (digitalWrite).

	Arguments:
		n (int): the current state represented in decimal
*/
void inc_or_dec(int n)
{	
	// Converts decimal to binary
    for (int i = 0; i < 5; i++) {
        if (n % 2) {
            LED[i] = HIGH;
        }
        else {
            LED[i] = LOW;
        }
        n = n / 2;
    }

    // Displays the current state
    for (int j = 0; j < 5; j++) {
    	digitalWrite(LEDPIN[j], LED[j]);
    }
}

int main()
{
	// Sets up the inputs and outputs
    setup();

    // Variables
    int inc_dec_counter = 0;
    int store_state = 0;
    int counter = 0;
    int check_hold_inc = HIGH;
    int check_hold_dec = HIGH;
    int check_hold_store = HIGH;

    /* 
    	When the increment button is pushed the value of the inc_dec_counter
    	goes up by 1. When the decrement button is pushed the value of
    	inc_ded_counter goes down by 1. The values are sent to the inc_or_dec
    	function to be convert to binary and then display the LED. An if statement
    	is added to only allow for a single button press.
    */
    while (true) {
        if (check_hold_inc != digitalRead(inc_button)) {
            if (digitalRead(inc_button) == LOW) {
                inc_dec_counter++;
                // delay needed to ensure stability
                delay(20);
                if (inc_dec_counter <= 31) {
                    inc_or_dec(abs(inc_dec_counter));
                }
                else {
                    inc_dec_counter = 0;
                    inc_or_dec(abs(inc_dec_counter));
                }
            }
            check_hold_inc = digitalRead(inc_button);
        }

        if (check_hold_dec != digitalRead(dec_button)) {
            if (digitalRead(dec_button) == LOW) {
                inc_dec_counter--;
                // delay needed to ensure stability
                delay(20);
                if ((inc_dec_counter <= 31) && (inc_dec_counter != 0)) {
                    inc_or_dec(abs(inc_dec_counter));
                }
                else if (inc_dec_counter == 0) {
                    inc_dec_counter = 32;
                    inc_or_dec(abs(inc_dec_counter));
                }
            }
            check_hold_dec = digitalRead(dec_button);
        }

        if (check_hold_store != digitalRead(store_button)) {
            if (digitalRead(store_button) == LOW) {
                counter++;
                // delay needed to ensure stability
                delay(20);
                if (counter == 1) {
                    store_state = inc_dec_counter;
                    inc_dec_counter = 0;
                    inc_or_dec(0);
                }
                else if (counter == 2) {
                    inc_or_dec(store_state);
                    counter = 0;
                    inc_dec_counter = store_state;
                }
            }
            check_hold_store = digitalRead(store_button);
        }
    }
}
