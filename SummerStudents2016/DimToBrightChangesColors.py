from LEDsetup import*
led.fill(Off)
led.update()



m = int(raw_input('how many times would you like it to blink? '))



for blink in range(m):
    for i in range(0,256):
            led.fill((i,0,0))
            led.update()

    for i in range(0,256):
            led.fill((146,i,0))
            led.update()
            
            
    for i in range(255,-1,-1):
            led.fill((i,146,0))
            led.update()


            
    for i in range(255,-1,-1):
            led.fill((0,i,0))
            led.update()

