from escpos.printer import Serial

p = Serial(devfile='COM1',
           baudrate=19200,
           bytesize=8,
           parity='N',
           stopbits=1,
           timeout=1.00,
           dsrdtr=False)
p.text("Hello World\n")
p.cut()
