int s1= A0; // Calling all sensors[autobots:)]
int s2= A1;
int s3= A2;
int s4= A3;
int s5= A4;
const int left = 6;  
const int right = 5; // for motors - 6 and 5 are PWm pins.
int lefts;
int rights; // motor speeds
float s;
float e1 = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(right, OUTPUT);
  pinMode(left, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int S1 = analogRead(A0); // weight = -2, rightmost sensor
  int S2 = analogRead(A1); // weight = -1, second to rightmost
  int S3 = analogRead(A2); // weight = 0, middle
  int S4 = analogRead(A3); // weight = 1, second to leftmost
  int S5 = analogRead(A4); // weight = 2, leftmost sensor
  int sum = (S1+S2+S3+S4+S5);
  float val = 0;
  

  if (sum !=0){
    val = float(S1*-2 + S2*-1 + S4*1 + S5*2)/float(sum);  // convert to float, as we get integer in normal division in C++
  } // only if not dividing by 0
  else{
    val = 0;
    s=0; // Go ahead, if entire surface is black
  }


  

  s = s+val; // to count accumulated error
  s = constrain(s,-100,100); // to limit accumulated error
  float d =  val- e1; // to find change in error
  e1 = val; 

  float PID_val = 20*val + 0.05*s + 10*d; // PID calculation

  if (sum<1000){
    lefts = 200+PID_val;
    rights = 200-PID_val;
    lefts = constrain(lefts, 0, 255);
    rights = constrain(rights, 0, 255);
    analogWrite(left, lefts );
    analogWrite(right, rights);
  }
  else{
    while (sum>1000){
      analogWrite(left, 180);
      analogWrite(right, 0);
  
      // re-read sensors to see if line comes back
      S1 = analogRead(A0);
      S2 = analogRead(A1);
      S3 = analogRead(A2);
      S4 = analogRead(A3);
      S5 = analogRead(A4);
      sum = S1 + S2 + S3 + S4 + S5;
      if (sum<1000){
        break;

      }
    }

  }
  
  
  


  Serial.println(val);
  delay(20);
}
  delay(20);
}
