const int ledRed = 5;
const int ledGreen = 6;
const int ledYellow = 7;

class LedController {
  	int capacity;
	int ledNumber;
	int *leds;
public:
  	LedController(int capacity) {
      	this -> capacity = capacity;
  		ledNumber = 0;
      	leds = new int[capacity];
  	}	
 	 ~LedController() {
  		delete [] leds;
  	}
  	bool addPin(int x);
  	void turnAllLEDs(uint8_t state = HIGH);
};

bool LedController::addPin(int x) {
  	int index = ledNumber;
  	if (index < capacity){
      	pinMode(x, OUTPUT);
  		leds[index] = x;
  		ledNumber += 1;
  		return true;
	}
 	return false;
}
void LedController::turnAllLEDs(uint8_t state){
  	for(int i = 0; i < ledNumber; i++){
		digitalWrite(leds[i], state);
    }
}


void setup() {
  	Serial.begin(9600);
}

void loop() {
  	LedController ledContr(200);

  	bool result = ledContr.addPin(ledRed);
  	if(!result){
    	Serial.println("No space for red LED");
    }
  	result = ledContr.addPin(ledGreen);
  	if(!result){
    	Serial.println("No space for green LED");
    }
  	result = ledContr.addPin(ledYellow);
  	if(!result){
    	Serial.println("No space for yellow LED");
    }

	ledContr.turnAllLEDs();
  	delay(1000);
    ledContr.turnAllLEDs(LOW);
  	delay(500);
  	Serial.println("Ala ma kota i arduino");
  	
}