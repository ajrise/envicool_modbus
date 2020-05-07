#define Fan_Speed_in 2   //定义测速端口
#define Fan_Speed_out 5  //定义输出端口
#include Serial




void setup()
{
  Serial.begin(9600);
  pinMode(pwm, OUTPUT);
  pinMode(fan_speed, INPUT);
}